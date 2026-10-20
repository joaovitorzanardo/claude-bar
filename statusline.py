#!/usr/bin/env python3
"""Status line do Claude Code: pasta, modelo, sessão (5h), semana (7d) e contexto."""
import json
import os
import sys
import time
from datetime import datetime

RESET = "\033[0m"
DIM = "\033[2m"
BLUE = "\033[01;34m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
DIAS = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]


def cor(pct):
    if pct < 60:
        return GREEN
    if pct < 90:
        return YELLOW
    return RED


def barra(pct, largura=10):
    pct = max(0.0, min(100.0, float(pct)))
    cheios = round(pct / 100 * largura)
    c = cor(pct)
    return f"{c}{'█' * cheios}{DIM}{'░' * (largura - cheios)}{RESET} {c}{pct:.0f}%{RESET}"


def tempo_restante(resets_at):
    seg = max(0, int(resets_at - time.time()))
    h, m = divmod(seg // 60, 60)
    return f"{h}h{m:02d}m" if h else f"{m}m"


def quando(resets_at):
    d = datetime.fromtimestamp(resets_at)
    return f"{DIAS[d.weekday()]} {d:%H:%M}"


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}

    partes = []

    cwd = (data.get("workspace") or {}).get("current_dir") or data.get("cwd") or os.getcwd()
    partes.append(f"{BLUE}📁 {os.path.basename(cwd.rstrip('/')) or cwd}{RESET}")

    modelo = (data.get("model") or {}).get("display_name")
    if modelo:
        partes.append(f"{CYAN}{modelo}{RESET}")

    limites = data.get("rate_limits") or {}

    sessao = limites.get("five_hour") or {}
    if sessao.get("used_percentage") is not None:
        txt = f"sessão {barra(sessao['used_percentage'])}"
        if sessao.get("resets_at"):
            txt += f" {DIM}↻ {tempo_restante(sessao['resets_at'])}{RESET}"
        partes.append(txt)

    semana = limites.get("seven_day") or {}
    if semana.get("used_percentage") is not None:
        txt = f"semana {barra(semana['used_percentage'])}"
        if semana.get("resets_at"):
            txt += f" {DIM}↻ {quando(semana['resets_at'])}{RESET}"
        partes.append(txt)

    ctx = (data.get("context_window") or {}).get("used_percentage")
    partes.append(f"ctx {barra(ctx or 0)}")

    print(f" {DIM}│{RESET} ".join(partes))


if __name__ == "__main__":
    main()
