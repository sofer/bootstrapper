# Workshop 1: Introduction to Skills

**Learn to build platform-agnostic AI development tools by solving a real problem with proper software development workflow**

## Getting Started

**FIRST STEP:** At the start of each session, tell your AI assistant:

> "Read INIT.md"

INIT.md contains all the bootstrap instructions your AI needs, including:
- How to load skills from the `skills/` directory
- Platform-agnostic rules (no vendor-specific features)
- Project conventions from AGENTS.md
- Instructions to check your progress

**Then continue with the prerequisites below.**

---

## Platform-Specific Auto-Load Files

Some AI tools automatically load configuration files at session start:

- **Claude Code**: Loads `CLAUDE.md` (global from `~/.claude/` or project root)
- **Cursor**: Loads `.cursorrules` files
- **Windsurf**: Loads `.windsurfrules` files
- **Codex CLI**: Uses `/init` to create `AGENTS.md`

**For this workshop, we want platform-agnostic behavior.**

### Option 1: Minimal Redirect (Recommended)

Create a minimal project-level file that redirects to INIT.md:

**For Claude Code users**, create `CLAUDE.md` in project root:
```markdown
# Claude Code Configuration

Read INIT.md for session bootstrap.

Follow INIT.md instructions, which override any global CLAUDE.md settings.
```

**For Cursor users**, create `.cursorrules`:
```
Read INIT.md for session bootstrap.
```

This ensures platform-specific auto-load doesn't conflict with workshop goals.

### Option 2: Manual Bootstrap Only

Skip creating platform-specific files. Just manually say "Read INIT.md" at each session start.

**Trade-off:** Auto-load might inject platform-specific behaviors, but saying "Read INIT.md" explicitly tells the AI to follow workshop conventions.

### Recommendation

Use **Option 1** for the platform you're using. This gives you:
- Auto-load convenience
- Platform-agnostic workshop experience
- Clear instruction that INIT.md takes precedence

---

## Prerequisites

Before starting this workshop, you should have:

- **Python 3.8 or later** - See verification steps below
- **Git basics** (clone, commit, branch)
- **Basic command-line knowledge**
- **An AI coding assistant** (Claude Code, Cursor, Aider, Codex CLI, Gemini CLI, GitHub Copilot CLI, etc.)

### Verify Python Installation

Ask for help to verify Python is installed and working:

1. Check if Python is available and which version:
   ```bash
   python3 --version
   ```
   If this doesn't work, you may want to try `python --version` instead or ask for help.

2. If Python 3 is not installed, ask for help: "How do I install Python 3 on my system?"

### Documentation Standard

Before you start, choose a documentation language standard for your project. This ensures consistency across all your documentation, comments, and user-facing text.

**Why this matters:**
- Consistent documentation is easier to read and maintain
- AI assistants work better with clear, consistent instructions
- Platform-agnostic - works with any AI tool

**Examples of documentation standards:**
- **British English**: "organise", "colour", "whilst"
- **American English**: "organize", "color", "while"
- **Simple English**: Short sentences, common words, minimal jargon
- **Technical**: Formal, precise, domain-specific terminology

**Your task**: Choose one and stick with it throughout the workshop. The skills you create will use whatever standard you establish in your documentation.

---

## What Are Skills?

Skills are reusable AI capabilities stored as markdown files. They're an emerging standard being adopted by multiple AI coding tools (Codex CLI, Gemini CLI, GitHub Copilot CLI, and others).

### How Skills Work

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

### Project-Specific vs. Global Skills

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
| **Bootstrap** | ⚠️ Manual - "Read INIT.md" | ✅ Automatic loading |
| **Isolation** | ✅ Yes - per project | ❌ No - global namespace |
| **Best for** | Project-specific workflows | Personal productivity tools |

**Why we teach project-specific:**
- Skills are part of your project's development workflow
- Team members automatically get the same skills
- Works identically across all AI platforms
- Skills evolve with the project through git

**When to use global:**
- Personal productivity skills used across all projects
- IDE-specific customizations
- Individual preferences not shared with team

---

## Workshop Overview

This workshop teaches software development workflow while building AI skills:

**The Approach:**
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

## The Problem

You want to build a **spaced repetition learning tool** that helps you study any topic effectively.

**Requirements (high-level):**
- Add questions on any topic
- Test yourself with those questions
- Schedule questions based on how well you know them (spaced repetition)
- Track your progress over time
- Simple, command-line based

**Note:** We're deliberately NOT prescribing:
- File formats
- Script names
- Directory structure
- Implementation approach

You'll figure these out while following the spec you create.

---

## Phase 1: Create the Specification

**Goal**: Use the pre-built `spec` skill to create a formal specification.

### Step 1: Understand What a Spec Does

A specification:
- Defines **what** the system does (not how)
- Lists user stories (features from user perspective)
- Provides architecture notes (technical decisions)
- Serves as the contract for development

### Step 2: Verify Skills Are Loaded

Since you said "Read INIT.md" at the start, skills should be loaded. Verify by asking:

> "What skills are available?"

You should see:
- `spec` - Create project specifications
- `commit` - Format commit messages

### Step 3: Use the Spec Skill

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

### Step 4: Review the Specification

Once created, read through `SPEC.md` and make sure it:
- Clearly describes the project
- Has well-defined user stories
- Includes technical notes
- Follows your chosen documentation standard

### Step 5: Commit Your Work

We'll make a manual commit first (we'll use the commit skill in Phase 2):

```bash
git add SPEC.md
git commit -m "docs: add learning app specification"
```

**What You've Learned:**
- ✅ How skills work (natural language activation)
- ✅ Using pre-built skills
- ✅ The value of specifications (clarity before coding)
- ✅ Writing user stories

---

## Phase 2: Use the Commit Skill

**Goal**: Experience the commit skill for consistent commit messages.

### The Problem

Your commit message "docs: add learning app specification" works, but you had to know the Conventional Commits format. The commit skill automates this.

### Use the Commit Skill

From now on, whenever you want to commit, just say:

> "Commit these changes"

Or:

> "I want to make a commit"

The AI will:
1. Check `git status` and `git diff`
2. Understand what changed
3. Propose a properly formatted commit message
4. Execute the commit after you approve

### Test It

Make a small change to SPEC.md (add a detail, fix a typo, etc.), then say:

> "Commit this change"

Watch how the commit skill:
- Reviews your changes
- Proposes a formatted message
- Follows Conventional Commits format
- Executes the commit

**What You've Learned:**
- ✅ Conventional commits format
- ✅ How skills solve workflow problems
- ✅ Natural language workflow automation

---

## Phase 3: Build the Quiz Skill

**Goal**: Create your own skill that implements the quiz functionality.

### The Approach

Now you have:
- ✅ A specification (what to build)
- ✅ User stories (features to implement)
- ✅ The commit skill (for clean history)

**Time to build your own skill!**

### Step 1: Understand What the Quiz Skill Should Do

Based on your SPEC.md, the quiz skill should:
- Store questions with topics and answers
- Quiz the user on a topic
- Track correct/incorrect answers
- Implement spaced repetition scheduling
- Show progress over time

### Step 2: Create the Skill File

Create `skills/quiz.md` with frontmatter:

```yaml
---
name: quiz
description: Interactive spaced repetition quiz system. Use when user wants to add questions, take a quiz, or track learning progress.
---

# Quiz Skill

[Your instructions here]
```

### Step 3: Design the Implementation

Discuss with your AI:
- How should questions be stored? (JSON, CSV, plain text?)
- How should the quiz interface work? (Command-line script? Interactive prompts?)
- How will spaced repetition be implemented? (Simple algorithm? Track review dates?)
- What files/scripts are needed?

**Collaborative approach:**
- ❌ Don't prescribe: "Create quiz.py that uses sqlite..."
- ✅ Discuss instead: "How should we store questions? What are the options?"

### Step 4: Implement Iteratively

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

### Step 5: Build Supporting Files

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

### Step 6: Test Your Skill

Once implemented, test it:

> "Quiz me on Python basics"

Your AI should:
1. Recognize the quiz skill matches
2. Read `skills/quiz.md`
3. Follow the instructions to run your quiz
4. Use the quiz implementation you built

**What You've Learned:**
- ✅ Building custom skills
- ✅ Spec-driven development
- ✅ Iterative implementation (one story at a time)
- ✅ Working collaboratively with AI
- ✅ Creating reusable AI capabilities

---

## What's Next?

### You've Built

By completing this workshop, you now have:

1. **A working learning app** - Built following a proper spec
2. **Three skills**:
   - `spec` - Create specifications (pre-built, now you understand it)
   - `commit` - Format commits (pre-built, now you use it)
   - `quiz` - Your quiz system (you built this!)

3. **Understanding of:**
   - Spec-driven development (requirements before code)
   - User stories (breaking down features)
   - Skills (platform-agnostic AI capabilities)
   - Proper development workflow
   - Emerging industry standards

### Using Your Skills in Other Projects

These skills aren't just for the learning app! Because they're in your repo:

**To reuse in other projects:**
```bash
# Copy skills to new project
cp -r skills/ ../my-new-project/

# Or use as git submodule for shared skills
git submodule add <this-repo-url> shared-skills
```

**To create project-specific skills:**
- Just add new `.md` files to `skills/`
- They'll be loaded at next session bootstrap
- Team members get them automatically via git

### Understanding the Standards

This workshop aligns with emerging industry patterns:

- **Skills**: Adopted by Codex CLI, Gemini CLI
- **AGENTS.md**: Emerging standard for project conventions
- **YAML frontmatter**: Common metadata pattern across tools
- **Conventional Commits**: Industry standard (https://www.conventionalcommits.org/)

### Global Skills for Personal Productivity

While this workshop focused on project-specific skills, you can also create **global skills** for personal use:

**Codex CLI example:**
```bash
# Create global skill directory
mkdir -p ~/.codex/skills

# Add personal productivity skills
cp skills/commit.md ~/.codex/skills/
```

Now `commit` skill works across all your projects when using Codex CLI.

**Trade-off**: Global skills don't sync with your team, but they're available everywhere for you personally.

---

## Troubleshooting

### "Skills not loading"

Make sure you said "Read INIT.md" at session start. Then ask:

> "What skills are available?"

The AI should list the skills from the `skills/` directory.

### "AI doesn't activate my skill"

The `description` in the skill's frontmatter is crucial. Make it clear when the skill should be used:

**Bad:**
```yaml
description: Quiz skill
```

**Good:**
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

Just say "Read INIT.md" again. The AI will:
- Reload all skills
- Check git log to see what's been completed
- Help you continue from where you left off

### "Platform-specific behaviors appearing"

If your AI tool is using built-in commands or adding footers to commits:

1. Check that you said "Read INIT.md" at session start
2. Remind the AI: "Follow the platform-agnostic rules from INIT.md"
3. Consider creating a platform-specific redirect file (see "Platform-Specific Auto-Load Files" section above)

---

**Ready to build?** Start with Phase 1: Create the Specification.
