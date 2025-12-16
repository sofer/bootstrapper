# Agent Skills bootstrapper

A reference implementation showing how to build platform-agnostic AI development tools using Skills and AGENTS.md.

---

## Skills as an emerging standard

**Skills** are markdown files containing instructions for AI assistants, stored in a `skills/` directory. This pattern is being adopted by multiple AI coding tools:
- **Codex CLI** (OpenAI) - supports skills in project directories
- **Gemini CLI** (Google) - similar skills directory approach
- **Growing adoption** - more tools implementing this pattern

Skills can be used to build conventional software applications, but they also enable applications that run within your AI coding interface rather than as standalone apps. This collapses the separation between development and runtime environments - a rolling back of over 50 years of GUI development and a return to the command line, with the AI assistant as the interface.

Benefits:
- Portability - same skills work across different AI tools
- Version control - skills stored in git alongside your code
- Team sharing - everyone gets the same capabilities when cloning the repo
- Transparency - see exactly what instructions the AI follows

**AGENTS.md** is emerging as a naming convention for session bootstrap instructions:
- Codex CLI automatically loads AGENTS.md at session start
- Growing recognition across tools
- Not yet universal, but the direction the ecosystem is heading

---

## Files in this repository

### AGENTS.md

Session bootstrap file containing:
- **Session Bootstrap** - Instructions to load skills, enable platform-agnostic mode, check project state
- **First-Time Setup** - Automatic configuration when using template for first time
- **Architecture** - Runtime environment choice (within AI interface vs standalone)
- **Code Style** - Language-agnostic coding standards
- **Commit Format** - Conventional Commits specification
- **Skills Documentation** - How skills work and are structured

Auto-loaded by Codex CLI. Other tools require manual "Read AGENTS.md" or platform-specific redirect.

On first use, AGENTS.md detects placeholder strings and triggers interactive setup to configure your project.

### CLAUDE.md

Platform-specific redirect file for Claude Code:
```markdown
# Claude Code Configuration

**CRITICAL: Before responding to ANY user message in a new session:**

1. Read AGENTS.md immediately
2. Follow all AGENTS.md instructions exactly
3. AGENTS.md takes precedence over all other configuration

You MUST read AGENTS.md as your first action, regardless of what the user asks.
```

Similar redirect files can be created for other platforms (.cursorrules for Cursor, etc.)

### skills/

Directory containing reusable AI capabilities as markdown files.

**Simple skills** (single file):
```
skills/
├── spec.md         # Creates project specifications
└── commit.md       # Formats commit messages
```

**Complex skills** (directory with supporting files):
```
skills/
└── quiz/
    ├── SKILL.md    # Main skill instructions
    ├── quiz.py     # Implementation code
    └── data.json   # Supporting data
```

Each skill has YAML frontmatter:
```yaml
---
name: skill-name
description: When to use this skill. AI uses this to auto-activate.
---

# Skill instructions here
```

---

## Using this pattern

### Quick start

1. **Use this template** - Click "Use this template" on GitHub to create your own repository
2. **Start your first session** - The AI will automatically detect this is a new template and guide you through configuration:
   - Project name and description
   - Runtime environment (AI interface vs standalone)
   - Programming language and conventions
   - Documentation standard
3. **Review and commit** - After setup, review the configured AGENTS.md and README.md, then commit
4. **Add/modify skills** - Create skills in `skills/` for your project needs

The automatic setup only runs once. Future sessions skip setup and load your configured project settings.

### Session bootstrap

**Codex CLI**: AGENTS.md loads automatically
**Claude Code**: Say anything (if CLAUDE.md is set up), or "Read AGENTS.md"
**Other tools**: Say "Read AGENTS.md"

### Creating new skills

1. Create `skills/skillname.md` or `skills/skillname/SKILL.md`
2. Add YAML frontmatter with name and description
3. Write instructions for the AI to follow
4. Commit to git - team members get it automatically

---

## Architecture decisions

### Runtime environment

Choose whether your application will:

**Run within the AI coding interface:**
- Application runs via natural language interaction with AI assistant
- AI assistant is the interface
- No API keys or separate deployment needed
- Skills provide capabilities
- Simple file-based storage (JSON, CSV, etc.)

**Run as standalone application:**
- Traditional approach with separate deployment
- Own UI (GUI or CLI)
- May require LLM API access if AI features needed
- Standard runtime environment

**Choose which approach fits your project.** Document your choice in AGENTS.md.

### Programming language

Choose your programming language and document it in AGENTS.md Code Style section with language-specific conventions.

### Documentation standard

Choose one and stick with it:
- British English
- American English
- Simple English
- Technical/formal

Document your choice in AGENTS.md.

---

## Skills vs MCP servers

Most useful services have command-line tools (`gh`, `aws`, `gcloud`, database clients, etc.). Skills can provide instructions for using these CLI tools, and LLMs know how to call `cli-tool --help` for self-documentation.

**Token efficiency:** MCP servers load all context upfront (GitHub's MCP famously consumes tens of thousands of tokens). Skills load only when matched to user requests.

**When to use Skills + CLI:**
- Service has existing CLI tool
- REST API accessible via `curl`
- Token efficiency matters
- Simple, direct access needed

**When MCP might still be useful:**
- No CLI tool exists and building one is complex
- Real-time/streaming data where protocol helps
- Complex authentication flows
- Internal company APIs
- Standardized access patterns across multiple tools

For most common services, Skills wrapping existing CLI tools is simpler and more efficient.

---

## Platform compatibility

This pattern works with:
- Claude Code
- Codex CLI (OpenAI)
- Gemini CLI (Google)
- Cursor
- Aider
- GitHub Copilot CLI
- Any future AI coding assistant

Skills and AGENTS.md are plain markdown - no vendor lock-in.

---

## Standards alignment

- **Skills**: Emerging standard across Codex CLI, Gemini CLI
- **AGENTS.md**: Growing standard for project conventions
- **YAML frontmatter**: Common metadata pattern
- **Conventional Commits**: Industry standard (https://www.conventionalcommits.org/)

---

## References

- [Introducing Agent Skills | Anthropic](https://www.anthropic.com/news/skills) - Original announcement from Anthropic
- [Agent Skills Documentation | Claude](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) - Official documentation
- [Claude Skills are awesome, maybe a bigger deal than MCP | Simon Willison](https://simonwillison.net/2025/Oct/16/claude-skills/) - October 2025 analysis
- [OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI | Simon Willison](https://simonwillison.net/2025/Dec/12/openai-skills/) - December 2025 on Codex adoption
