# claude-bar

Status line do Claude Code que mostra: pasta atual, modelo, uso da sessão (5h) com tempo até redefinir, uso da semana (7d) com dia/horário de redefinição e uso do contexto.

```
📁 projeto │ Opus 5.5 │ sessão ███░░░░░░░ 30% ↻ 2h15m │ semana █░░░░░░░░░ 12% ↻ seg 09:00 │ ctx ██░░░░░░░░ 20%
```

## Instalação

Requer Python 3.

```bash
git clone https://github.com/joaovitorzanardo/claude-bar.git ~/claude-bar
~/claude-bar/install.sh
```

O script cria um symlink `~/.claude/statusline.py` → `statusline.py` deste repo e adiciona a chave `statusLine` em `~/.claude/settings.json` (preservando o resto). Para atualizar depois: `git -C ~/claude-bar pull`.
