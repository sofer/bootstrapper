# Agent Skills bootstrapper

A reference implementation showing how to build portable AI workflows using Skills and AGENTS.md. Works best for teams using multiple AI tools and projects with 3-10 well-defined skills.

---

## Skills as an emerging standard

**Skills** are markdown files containing instructions for AI assistants, stored in a `skills/` directory. This pattern is being adopted by multiple AI coding tools:
- **Codex CLI** (OpenAI) - supports skills in project directories
- **Gemini CLI** (Google) - similar skills directory approach
- **Growing adoption** - more tools implementing this pattern

Skills provide reusable AI behaviors and workflows. They can support both conventional software development and projects where natural language interaction with the AI assistant is the primary interface.

Benefits:
- **Portability** - Skill content (markdown) works across different AI tools
- **Minimal integration** - One redirect file per tool (CLAUDE.md, .cursorrules, etc.)
- **Version control** - Skills stored in git alongside your code
- **Team sharing** - Everyone gets the same capabilities when cloning the repo
- **Transparency** - See exactly what instructions the AI follows
- **Simplicity** - No build process, no dependencies, just markdown

**AGENTS.md** is emerging as a naming convention for session bootstrap instructions:
- Codex CLI automatically loads AGENTS.md at session start
- Growing recognition across tools
- Not yet universal, but the direction the ecosystem is heading

---

## Files in this repository

### AGENTS.md

**Streamlined** session bootstrap file (237 lines) containing:
- **Session Bootstrap** - Instructions to load skills, enable platform-agnostic mode, check project state
- **Architecture** - Runtime environment choice (within AI interface vs standalone)
- **Code Style** - Language-agnostic coding standards
- **Testing** - Framework conventions
- **Commit Format** - Conventional Commits specification
- **Skills Documentation** - How skills work and are structured

Auto-loaded by Codex CLI. Other tools require manual "Read AGENTS.md" or platform-specific redirect.

On first use, AGENTS.md detects placeholder markers and references SETUP.md for interactive configuration.

### SETUP.md

First-time setup guide for AI assistants. This file is only read when AGENTS.md contains placeholder markers.

Contains detailed instructions for:
- Interactive question flow (project name, language, runtime, etc.)
- File update procedures
- Edge case handling
- Configuration completion

Separating setup from AGENTS.md keeps the bootstrap file scannable and efficient.

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

## For Learners

New to AI-assisted development? This template makes it easy to get started.

### Starting Each Session

At the start of every session with any AI coding assistant:

**For Claude Code users** (if you've set up `CLAUDE.md`):
- Just say **anything** to start - "hello", "let's begin", or ask a question
- CLAUDE.md automatically triggers AGENTS.md loading

**For Codex CLI users**:
- AGENTS.md is automatically loaded - just start working
- No special command needed

**For other AI tools** (Gemini CLI, Cursor, Aider, etc.):
- Say: **"Read AGENTS.md"**
- This loads all project conventions and skills

### What This Does

When AGENTS.md is loaded, your AI assistant will:
1. Load all available skills from the `skills/` directory
2. Enable platform-agnostic mode (no vendor-specific features)
3. Check your current progress via git
4. List available skills
5. Get ready to help with your project

### Using Skills

You don't need special syntax. Just talk naturally:

- "Create a spec for a task manager app" → AI activates spec skill
- "I want to commit these changes" → AI activates commit skill
- "Help me add a feature" → AI uses project conventions

The AI automatically matches your request to the appropriate skill based on the skill descriptions.

### Session Resume

Since conversations may be interrupted:
- Git tracks completed work
- AGENTS.md reloads all context in new sessions
- AI checks git log to see your progress
- You can continue from where you left off

Just say "Read AGENTS.md" again (or rely on auto-load for Claude Code/Codex) to re-establish context in a new session.

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

## Limitations and Considerations

This approach has specific strengths and limitations. Understanding them helps you decide when to adopt this pattern.

### What This Approach Is Great For

✅ **Teams using multiple AI tools** - Provides consistency across Claude Code, Codex CLI, Cursor, etc.
✅ **Small to medium projects** - Works well with 3-10 skills
✅ **Educational purposes** - Demonstrates portable AI workflows
✅ **Shared team conventions** - Git-versioned, auditable AI instructions
✅ **Reference implementation** - Learn how platform-agnostic skills work

### When NOT to Use This Approach

❌ **Your team uses only one AI tool** - Better to use that tool's native features (Claude Projects, Cursor rules, etc.) for maximum power
❌ **You need 20+ skills** - Discovery becomes unwieldy; matching gets unreliable
❌ **Performance-critical workflows** - Reading all skills every session has overhead
❌ **Complex stateful applications** - Skills are stateless instructions, not full applications
❌ **Individual developer, simple needs** - Might be overhead vs just good prompts

### Important Clarifications

**"Platform-agnostic" has limits:**
- ✅ Content is portable (markdown works everywhere)
- ⚠️ Integration requires per-tool setup (CLAUDE.md, .cursorrules, etc.)
- Better described as: "Portable workflows with minimal per-tool glue"

**Skills are not applications:**
- Skills provide reusable AI behaviors and instructions
- They don't have persistent state or traditional application lifecycle
- Think "AI workflows" not "apps that run in AI interface"

**Skill discovery scales to ~10 skills:**
- Natural language matching works well for small skill sets
- Beyond 10 skills, consider categorization or explicit invocation
- Reading all skills every session becomes inefficient at scale

### Complementary Approaches

Don't make it either/or:
- **Skills + MCP servers** - Use skills for instructions, MCP for actual capabilities
- **Skills + native features** - Use platform-agnostic skills for core conventions, native features for tool-specific enhancements
- **Hybrid approach** - Core conventions in AGENTS.md, tool-specific optimizations where beneficial

### Sweet Spot

This approach works best for:
- 3-10 well-defined skills
- Teams working across 2-3 different AI tools
- Projects prioritizing portability and transparency
- Educational or reference implementations

If your needs fall outside this sweet spot, consider alternatives or hybrid approaches.

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
