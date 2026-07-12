#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CLAUDE_DEST="$HOME/.claude/skills/life-designer-pro"
CODEX_DEST="$HOME/.agents/skills/life-designer-pro"

install_skill() {
  local dest="$1"
  mkdir -p "$dest"
  cp "$REPO_ROOT/SKILL.md" "$dest/SKILL.md"
  rm -rf "$dest/references" "$dest/templates" "$dest/prompts"
  cp -R "$REPO_ROOT/references" "$dest/references"
  cp -R "$REPO_ROOT/templates" "$dest/templates"
  cp -R "$REPO_ROOT/prompts" "$dest/prompts"
}

install_skill "$CLAUDE_DEST"
install_skill "$CODEX_DEST"
mkdir -p "$CODEX_DEST/agents"
cp "$REPO_ROOT/.agents/skills/life-designer-pro/agents/openai.yaml" "$CODEX_DEST/agents/openai.yaml"

echo "Installed Life Designer Pro skill for Claude Code and Codex."
echo "Claude: $CLAUDE_DEST"
echo "Codex:  $CODEX_DEST"
