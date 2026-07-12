$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$ClaudeDest = Join-Path $HOME ".claude/skills/life-designer-pro"
$CodexDest = Join-Path $HOME ".agents/skills/life-designer-pro"

function Install-Skill([string]$Destination) {
    New-Item -ItemType Directory -Force -Path $Destination | Out-Null
    Copy-Item (Join-Path $RepoRoot "SKILL.md") (Join-Path $Destination "SKILL.md") -Force

    foreach ($Folder in @("references", "templates", "prompts")) {
        $Target = Join-Path $Destination $Folder
        if (Test-Path $Target) { Remove-Item $Target -Recurse -Force }
        Copy-Item (Join-Path $RepoRoot $Folder) $Target -Recurse -Force
    }
}

Install-Skill $ClaudeDest
Install-Skill $CodexDest
$AgentsDest = Join-Path $CodexDest "agents"
New-Item -ItemType Directory -Force -Path $AgentsDest | Out-Null
Copy-Item (Join-Path $RepoRoot ".agents/skills/life-designer-pro/agents/openai.yaml") (Join-Path $AgentsDest "openai.yaml") -Force

Write-Host "Installed Life Designer Pro skill for Claude Code and Codex."
Write-Host "Claude: $ClaudeDest"
Write-Host "Codex:  $CodexDest"
