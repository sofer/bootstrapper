# Agent Skills Bootstrapper

A template for building portable AI workflows using skills and AGENTS.md. Currently works with Claude Code and Codex CLI.

## What is this?

**Skills** are markdown files containing instructions for AI assistants, stored in a `skills/` directory. This pattern is being adopted by multiple AI coding tools (Codex CLI, Gemini CLI, and others).

**AGENTS.md** is a session bootstrap file that loads skills and project conventions when an AI assistant starts working with your project.

This template provides:
- Auto-configuration on first use
- Example skills (spec, commit)
- Works with Claude Code and Codex CLI
- Git-versioned AI instructions

## What this demonstrates

1. **Cross-platform Agent Skills** - Works with both Claude Code and Codex CLI
2. **AGENTS.md convention** - Standard file loaded at session start
3. **Example skills** - Starter skills (spec, commit) to use as templates
4. **Interactive setup** - SETUP.md prompt file for project configuration

## What's in this repo?

- **AGENTS.md** - Session bootstrap file with project conventions, auto-loaded by some tools
- **SETUP.md** - First-time configuration guide (AI-readable, runs automatically on template use)
- **CLAUDE.md / GEMINI.md** - Platform-specific redirects to load AGENTS.md
- **skills/** - Directory for reusable AI capabilities
  - `spec.md` - Create project specifications
  - `commit.md` - Format commit messages

## How to use

1. **Use this template** - Create your repo from this template
2. **Start a session** - AI detects new template and guides you through setup (project name, language, runtime, etc.)
3. **Work naturally** - AI loads skills automatically, use them via natural language
4. **Add skills** - Create `skills/skillname.md` with YAML frontmatter + instructions

### Starting sessions

- **Codex CLI**: AGENTS.md loads automatically
- **Claude Code**: Say anything (CLAUDE.md redirects) or "Read AGENTS.md"
- **Other tools**: Say "Read AGENTS.md"

### Creating skills

```yaml
---
name: skill-name
description: When to use this skill
---

# Instructions for AI to follow
```

Skills can be simple (single `.md` file) or complex (directory with `SKILL.md` + supporting files).

## How it works

1. AI reads AGENTS.md at session start
2. Loads all skills from `skills/` directory
3. Matches user requests to skill descriptions
4. Follows skill instructions when activated
5. Uses project conventions from AGENTS.md

**Compatibility approach**: Codex CLI natively uses AGENTS.md + `skills/`. Claude Code requires a redirect file (CLAUDE.md) and symlink (.claude/skills). GEMINI.md is included for future compatibility.

## References

- [Introducing Agent Skills | Anthropic](https://www.anthropic.com/news/skills)
- [Agent Skills Documentation | Claude](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Conventional Commits](https://www.conventionalcommits.org/)
