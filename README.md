# Workshop 1: Introduction to Skills

**Learn to build platform-agnostic AI development tools by solving a real problem with proper software development workflow**

---

## Skills as an emerging standard

The AI coding assistant ecosystem is rapidly evolving, and **Skills** are emerging as a standard pattern across different AI tools.

### What are Skills?

**Skills** are markdown files containing instructions for AI assistants, stored in a `skills/` directory. This pattern is being adopted by multiple AI coding tools:
- **Codex CLI** (OpenAI) - supports skills in `~/.codex/skills/` and project directories
- **Gemini CLI** (Google) - similar skills directory approach
- **Growing adoption** - more tools implementing this pattern

Skills provide:
- **Portability** - same skills work across different AI tools
- **Version control** - skills stored in git alongside your code
- **Team sharing** - everyone gets the same capabilities when cloning the repo
- **Transparency** - see exactly what instructions the AI follows

### AGENTS.md - naming convention for session bootstrap

**AGENTS.md** is also emerging as a naming convention for the initial instructions that bootstrap an AI coding interface at the start of a session:
- **Codex CLI** - automatically loads AGENTS.md at session start
- **Growing recognition** - other tools beginning to adopt this naming convention
- **Not yet universal** - but the direction the ecosystem is heading

AGENTS.md typically contains session bootstrap instructions plus project conventions:
- How to load skills from the project's `skills/` directory
- Project coding standards and conventions
- Tool and framework preferences
- Commit message formats

### Workshop goal

This workshop teaches you to set up a portable AI development environment that works regardless of which AI CLI tool you're using - Claude Code, Codex CLI, Gemini CLI, Cursor, Aider, or future tools.

You'll learn to:
- Create skills that work across all AI platforms
- Use AGENTS.md for project conventions
- Build tools your team can share through git
- Avoid vendor lock-in by following emerging standards

The result: Skills and workflows that work today and will continue working as the ecosystem evolves.

---

## Getting started

First step: Bootstrap your session with AGENTS.md:

**For Claude Code users** (if you've set up `CLAUDE.md` as shown below):
- Just say **anything** to start - "hello", "let's begin", or ask a question
- CLAUDE.md automatically triggers AGENTS.md loading

**For Codex CLI users**:
- AGENTS.md is automatically loaded - just start working

**For other AI tools** (Gemini CLI, Cursor, Aider, etc.):
- Say: **"Read AGENTS.md"**

AGENTS.md contains all the bootstrap instructions your AI needs:
- How to load skills from the `skills/` directory
- Platform-agnostic rules (no vendor-specific features)
- Project conventions and coding standards
- Instructions to check your progress

Then continue with the prerequisites below.

---

## Platform-specific auto-load files

Some AI tools automatically load configuration files at session start:

- **Claude Code**: Loads `CLAUDE.md` (global from `~/.claude/` or project root)
- **Cursor**: Loads `.cursorrules` files
- **Windsurf**: Loads `.windsurfrules` files
- **Codex CLI**: Uses `/init` to create `AGENTS.md`

For this workshop, we want platform-agnostic behavior.

### Option 1: minimal redirect (recommended for Claude Code)

Create a minimal project-level file that redirects to AGENTS.md:

**For Claude Code users**, create `CLAUDE.md` in project root:
```markdown
# Claude Code Configuration

**CRITICAL: Before responding to ANY user message in a new session:**

1. Read AGENTS.md immediately
2. Follow all AGENTS.md instructions exactly
3. AGENTS.md takes precedence over all other configuration

You MUST read AGENTS.md as your first action, regardless of what the user asks.
```

**For Cursor users**, create `.cursorrules`:
```
Read AGENTS.md for session bootstrap.
```

**For Codex CLI users**, no redirect needed - AGENTS.md is automatically loaded.

This ensures platform-specific auto-load doesn't conflict with workshop goals.

### Option 2: manual bootstrap only

Skip creating platform-specific files. Just manually say "Read AGENTS.md" at each session start.

**Trade-off:** Auto-load might inject platform-specific behaviors, but saying "Read AGENTS.md" explicitly tells the AI to follow workshop conventions.

### Recommendation

Use **Option 1** for the platform you're using. This gives you:
- Auto-load convenience (for Claude Code/Codex CLI)
- Platform-agnostic workshop experience
- Clear instruction that AGENTS.md takes precedence

---

## Prerequisites

Before starting this workshop, you should have:

- **Python 3.8 or later** - See verification steps below
- **Git basics** (clone, commit, branch)
- **Basic command-line knowledge**
- **An AI coding assistant** (Claude Code, Cursor, Aider, Codex CLI, Gemini CLI, GitHub Copilot CLI, etc.)

### Verify Python installation

Ask for help to verify Python is installed and working:

1. Check if Python is available and which version:
   ```bash
   python3 --version
   ```
   If this doesn't work, you may want to try `python --version` instead or ask for help.

2. If Python 3 is not installed, ask for help: "How do I install Python 3 on my system?"

### Documentation standard

Before you start, choose a documentation language standard for your project. This ensures consistency across all your documentation, comments, and user-facing text.

Why this matters:
- Consistent documentation is easier to read and maintain
- AI assistants work better with clear, consistent instructions
- Platform-agnostic - works with any AI tool

Examples of documentation standards:
- **British English**: "organise", "colour", "whilst"
- **American English**: "organize", "color", "while"
- **Simple English**: Short sentences, common words, minimal jargon
- **Technical**: Formal, precise, domain-specific terminology

Your task: Choose one and stick with it throughout the workshop.

Where to document your choice:
1. Open `AGENTS.md` in the project root
2. Find the "Documentation" subsection under "Code Style"
3. Replace the first bullet point with your choice (e.g., "Documentation Standard: British English")
4. You can edit the file directly or ask your AI: "Update AGENTS.md with American English as the documentation standard"
5. The AI will reference this when creating skills and documentation

The skills you create will follow whatever standard you document in AGENTS.md.

---

## What are Skills?

Skills are reusable AI capabilities stored as markdown files. They're an emerging standard being adopted by multiple AI coding tools (Codex CLI and Gemini CLI have confirmed support, with others likely to follow).

### How Skills work

1. **Stored as markdown files** with YAML frontmatter:
   ```yaml
   ---
   name: commit
   description: Format commit messages. Use when user wants to commit changes.
   ---

   [Instructions for what the skill does...]
   ```

2. **Loaded at session start** - All skill descriptions loaded into AI's memory

3. **Activated by natural language** - No special syntax needed:
   - "Create a spec for my project" → AI matches to spec skill
   - "I want to commit these changes" → AI matches to commit skill
   - "Quiz me on Python" → AI matches to quiz skill

4. **Platform agnostic** - Same skills work in Claude Code, Cursor, Aider, Codex CLI, Gemini CLI, GitHub Copilot CLI, etc.

### Why Skills?

- **Portable**: Take your tools to any AI platform
- **Inspectable**: See exactly what instructions the AI follows
- **Customizable**: Edit the markdown files to change behavior
- **Shareable**: Team members get skills when they clone the repo
- **Versioned**: Store in git like any code
- **No lock-in**: Not dependent on any single AI vendor
- **Emerging standard**: Aligns with industry patterns

### Project-specific vs. global Skills

This workshop teaches **project-specific skills** stored in your repository:

```
my-project/
└── skills/          # In repo, versioned with git
    ├── spec.md
    ├── commit.md
    └── quiz.md
```

**Trade-offs:**

| Aspect | Project-Specific (This Workshop) | Global (Built-in CLI) |
|--------|----------------------------------|----------------------|
| **Location** | `./skills/` in project repo | `~/.codex/skills` or similar |
| **Git versioning** | ✅ Yes - committed with code | ❌ No - outside repo |
| **Team sharing** | ✅ Yes - clone repo, get skills | ❌ No - each person configures |
| **Platform agnostic** | ✅ Yes - same structure everywhere | ❌ No - different per tool |
| **Bootstrap** | ⚠️ Manual - "Read AGENTS.md" | ✅ Automatic loading |
| **Isolation** | ✅ Yes - per project | ❌ No - global namespace |
| **Best for** | Project-specific workflows | Personal productivity tools |

Why we teach project-specific:
- Skills are part of your project's development workflow
- Team members automatically get the same skills
- Works identically across all AI platforms
- Skills evolve with the project through git

When to use global:
- Personal productivity skills used across all projects
- IDE-specific customizations
- Individual preferences not shared with team

---

## Workshop overview

This workshop teaches software development workflow while building AI skills.

The approach:
1. Start with a problem
2. Write a specification (using pre-built spec skill)
3. Break into user stories
4. Build iteratively (creating a quiz skill)
5. Use clean commit messages (using pre-built commit skill)

By the end, you'll have:
- A working spaced repetition learning app
- Experience using skills (spec, commit)
- Your own quiz skill for ongoing learning
- Understanding of platform-agnostic AI development
- Transferable patterns that work with any AI tool

---

## The problem

You want to build a **spaced repetition learning tool** that helps you study any topic effectively.

Requirements (high-level):
- Add questions on any topic
- Test yourself with those questions
- Schedule questions based on how well you know them (spaced repetition)
- Track your progress over time
- Simple, command-line based
- Works within your AI coding interface (no API tokens, authentication, or standalone app infrastructure needed)

Note: We're deliberately NOT prescribing:
- File formats
- Script names
- Directory structure
- Implementation approach

You'll figure these out while following the spec you create.

---

## Phase 1: create the specification

Goal: Use the pre-built `spec` skill to create a formal specification.

### Step 1: understand what a spec does

A specification:
- Defines **what** the system does (not how)
- Lists user stories (features from user perspective)
- Provides architecture notes (technical decisions)
- Serves as the contract for development

### Step 2: verify Skills are loaded

Since AGENTS.md was loaded at session start, skills should be loaded. Verify by asking:

> "What skills are available?"

You should see:
- `spec` - Create project specifications
- `commit` - Format commit messages

### Step 3: use the spec skill

Just talk naturally. Say:

> "Create a spec for the learning app"

Or:

> "I want to create a specification"

The AI will:
1. Recognize this matches the spec skill description
2. Read and follow `skills/spec.md`
3. Help you create a specification
4. Save it to `SPEC.md`

Work with the AI to define:
- What the learning app does
- User stories (e.g., "As a learner, I want to add questions so that I can study them later")
- Technical approach (at high level - file-based? Database? How does spaced repetition work?)

### Step 4: review the specification

Once created, read through `SPEC.md` and make sure it:
- Clearly describes the project
- Has well-defined user stories
- Includes technical notes
- Follows your chosen documentation standard

### Step 5: commit your work

Now use the commit skill to commit your specification:

> "Commit these changes"

The AI will:
1. Check `git status` and `git diff`
2. Understand what changed (SPEC.md was created)
3. Propose a properly formatted commit message (e.g., "docs: add learning app specification")
4. Execute the commit after you approve

This demonstrates natural language workflow automation - no need to manually format commit messages.

What you've learned:
- ✅ How skills work (natural language activation)
- ✅ Using pre-built skills (spec and commit)
- ✅ The value of specifications (clarity before coding)
- ✅ Writing user stories
- ✅ Conventional Commits format via commit skill

Phase 1 complete. Ready to build your own skill in Phase 2?

---

## Phase 2: build the quiz skill

Goal: Create your own skill that implements the quiz functionality.

### The approach

Now you have:
- A specification (what to build)
- User stories (features to implement)
- The commit skill (for clean history)

Time to build your own skill.

### Step 1: understand what the quiz skill should do

Based on your SPEC.md, the quiz skill should:
- Store questions with topics and answers
- Quiz the user on a topic
- Track correct/incorrect answers
- Implement spaced repetition scheduling
- Show progress over time

### Step 2: create the skill file

Create `skills/quiz.md` with frontmatter:

```yaml
---
name: quiz
description: Interactive spaced repetition quiz system. Use when user wants to add questions, take a quiz, or track learning progress.
---

# Quiz Skill

[Your instructions here]
```

### Step 3: design the implementation

Discuss with your AI:
- How should questions be stored? (JSON, CSV, plain text?)
- How should the quiz interface work? (Command-line script? Interactive prompts?)
- How will spaced repetition be implemented? (Simple algorithm? Track review dates?)
- What files/scripts are needed?

Collaborative approach:
- ❌ Don't prescribe: "Create quiz.py that uses sqlite..."
- ✅ Discuss instead: "How should we store questions? What are the options?"

### Step 4: implement iteratively

Work through your user stories one at a time:

1. **Pick the first user story** from SPEC.md
2. **Implement that feature** (collaborate with AI on approach)
3. **Test it manually** (run it, make sure it works)
4. **Commit using commit skill**: "Commit these changes"
5. **Move to next story**

After each story, use the commit skill:
```
You: "Commit these changes"
AI: [Analyzes changes, proposes: "feat(quiz): add ability to store questions"]
AI: [Executes commit after your approval]
```

### Step 5: build supporting files

Your quiz skill might reference:
- Python scripts for quiz logic
- Data files for storing questions
- Helper utilities

You can organize these as:
```
skills/
└── quiz/
    ├── SKILL.md          # Main skill instructions
    ├── quiz.py           # Quiz implementation
    ├── questions.json    # Question storage
    └── spaced_rep.py     # Spaced repetition algorithm
```

Or keep it simple:
```
skills/
└── quiz.md               # Simple skill file
quiz.py                   # Implementation at project root
questions.json            # Data at project root
```

Choose based on your needs.

### Step 6: test your skill

Once implemented, test it:

> "Quiz me on Python basics"

Your AI should:
1. Recognize the quiz skill matches
2. Read `skills/quiz.md`
3. Follow the instructions to run your quiz
4. Use the quiz implementation you built

What you've learned:
- ✅ Building custom skills
- ✅ Spec-driven development
- ✅ Iterative implementation (one story at a time)
- ✅ Working collaboratively with AI
- ✅ Creating reusable AI capabilities

Phase 2 complete. Workshop finished.

---

## What's next?

### You've built

By completing this workshop, you now have:

1. **A working learning app** - Built following a proper spec
2. **Skills mastered**:
   - `spec` - Create specifications (pre-built)
   - `commit` - Format commits (pre-built)
   - `quiz` - Your quiz system (you built this!)

3. **Understanding of:**
   - Spec-driven development (requirements before code)
   - User stories (breaking down features)
   - Skills (platform-agnostic AI capabilities)
   - Proper development workflow
   - Emerging industry standards

### Using your Skills in other projects

These skills aren't just for the learning app! Because they're in your repo:

To reuse in other projects:
```bash
# Copy skills to new project
cp -r skills/ ../my-new-project/

# Or use as git submodule for shared skills
git submodule add <this-repo-url> shared-skills
```

To create project-specific skills:
- Just add new `.md` files to `skills/`
- They'll be loaded at next session bootstrap
- Team members get them automatically via git

### Understanding the standards

This workshop aligns with emerging industry patterns:

- **Skills**: Adopted by Codex CLI, Gemini CLI
- **AGENTS.md**: Emerging standard for project conventions
- **YAML frontmatter**: Common metadata pattern across tools
- **Conventional Commits**: Industry standard (https://www.conventionalcommits.org/)

### Global Skills for personal productivity

While this workshop focused on project-specific skills, you can also create **global skills** for personal use:

Codex CLI example:
```bash
# Create global skill directory
mkdir -p ~/.codex/skills

# Add personal productivity skills
cp skills/commit.md ~/.codex/skills/
```

Claude Code example:
```bash
# Create global skill directory
mkdir -p ~/.claude/skills

# Add personal productivity skills
cp skills/commit.md ~/.claude/skills/
```

Now `commit` skill works across all your projects when using that CLI tool.

Trade-off: Global skills don't sync with your team, but they're available everywhere for you personally.

---

## Troubleshooting

### "Skills not loading"

Make sure AGENTS.md was loaded at session start. Then ask:

> "What skills are available?"

The AI should list the skills from the `skills/` directory.

### "AI doesn't activate my skill"

The `description` in the skill's frontmatter is crucial. Make it clear when the skill should be used:

Bad:
```yaml
description: Quiz skill
```

Good:
```yaml
description: Interactive quiz system for learning. Use when user wants to add questions, take a quiz, or review learning progress.
```

### "Skill works in one AI tool but not another"

This shouldn't happen with properly formatted skills. Check:
- YAML frontmatter is valid
- Markdown is plain (no tool-specific syntax)
- No tool-specific commands in the instructions

If it still fails, file an issue - platform agnosticism is a core goal.

### "Session lost, how do I resume?"

Just say "Read AGENTS.md" again. The AI will:
- Reload all skills
- Check git log to see what's been completed
- Help you continue from where you left off

### "Platform-specific behaviors appearing"

If your AI tool is using built-in commands or adding footers to commits:

1. Check that AGENTS.md was loaded at session start (or manually say "Read AGENTS.md")
2. Remind the AI: "Follow the platform-agnostic rules from AGENTS.md"
3. Consider creating a platform-specific redirect file (see "Platform-Specific Auto-Load Files" section above)

---

Ready to build? Start with Phase 1: create the specification.
