# Workshop 1: Introduction to Prompt-Commands

**Learn to build AI-agnostic development tools by solving a real problem with proper software development workflow**

## Getting Started

**FIRST STEP:** At the start of each session, tell your AI assistant:

> "Read INIT.md"

INIT.md contains all the bootstrap instructions your AI needs, including:
- Platform-agnostic rules (no vendor-specific features)
- The `>name` prompt-command convention
- Instructions to read this README and check git log

**Then continue with the prerequisites below.**

---

## Prerequisites

Before starting this workshop, you should have:

- **Python installed** (version 3.8 or later)
- **Git basics** (clone, commit, branch)
- **Basic command-line knowledge**
- **An AI coding assistant** (Claude Code, Aider, Cursor, etc.)

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

**Your task**: Choose one and stick with it throughout the workshop. When you create prompts in later phases, your AI will follow whatever standard you establish in your documentation.

## What Are Prompt-Commands?

Prompt-commands are plain markdown files that tell your AI assistant what to do. They're our name for a simple, platform-agnostic way to store and reuse prompts.

### How They Compare to Slash Commands

**Slash Commands (Claude Code-specific)**
- Built into Claude Code
- Vendor-specific feature
- Only work in Claude Code
- Example: `/commit` to create a git commit

**Prompt-Commands (Platform-agnostic)**
- Plain markdown files you create
- Work with any AI assistant
- Stored in your project as `.md` files
- Invoked by typing `>name` in conversation
- Example: `>spec` to create a specification

### How They Work

1. You create a prompt file: `prompts/commit.md`
2. You invoke it in conversation: `>commit`
3. Your AI runs `python prompt.py commit` to read the prompt
4. Your AI follows the instructions in the prompt

The `prompt.py` utility handles finding and reading prompts automatically.

### Why Use Prompt-Commands?

- **Portable**: Take your tools to any AI platform
- **Inspectable**: See exactly what instructions the AI follows
- **Customisable**: Edit the markdown files to change behaviour
- **Shareable**: Team members can use the same prompts
- **Versioned**: Store in git like any code
- **No lock-in**: Not dependent on any single AI vendor

## Workshop Overview

This workshop teaches software development workflow while building prompt-command infrastructure:

**The Approach:**
1. Start with a problem
2. Write a specification
3. Break into user stories
4. Build iteratively

By the end, you'll have:
- A working spaced repetition learning app
- Two reusable prompts (`>spec`, `>commit`)
- Experience with spec-driven development
- Platform-agnostic tools you can use in any project

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

You and your AI will figure these out while following the spec you create.

## Phase 1: Create the Specification

**Goal**: Build a `>spec` prompt and use it to create a formal specification.

### Step 1: Understand What a Spec Does

A specification:
- Defines **what** the system does (not how)
- Lists user stories (features from user perspective)
- Provides architecture notes (technical decisions)
- Serves as the contract for development

### Step 2: Create `prompts/spec.md`

Create a directory and file:
```bash
mkdir -p prompts
```

Then work with your AI to create `prompts/spec.md` with these instructions:

```markdown
# Specification Writer

When the user asks to create or update a specification, help them:

1. **Project Specification**
   - High-level project goals
   - What problem does it solve?
   - Who is it for?

2. **User Stories**
   - Format: "As a [user type], I want [goal] so that [benefit]"
   - Create checkbox list for tracking: - [ ] Story description
   - Keep stories small and implementable

3. **Architecture & Technical Notes**
   - How does it work (high-level)?
   - What are the key components?
   - Any important design decisions

Follow the project's chosen documentation standard for all text.

Based on README Structure Template from project standards.
```

### Step 3: Use the Spec Prompt

In conversation with your AI:

1. Type: `>spec`
2. Your AI will read `prompts/spec.md` (via `python prompt.py spec`)
3. Work with your AI to create a specification for the learning app
4. Save the spec in `SPEC.md` or add it to a project README

The spec should include:
- What the learning app does
- User stories (e.g., "As a learner, I want to add questions so that I can study them later")
- Technical approach (at high level - file-based? Database? How does spaced repetition work?)

### Step 4: Commit Your Work

Make a manual commit (we'll improve this in Phase 2):
```bash
git add prompts/spec.md SPEC.md
git commit -m "add spec prompt and learning app specification"
```

**What You've Learned:**
- ✅ How to create a prompt-command
- ✅ How to invoke it with `>name`
- ✅ The value of specifications (clarity before coding)
- ✅ Writing user stories

## Phase 2: Create the Commit Prompt

**Goal**: Build a `>commit` prompt for consistent commit messages.

### The Problem

Your commit message "add spec prompt and learning app specification" works, but:
- No consistent format across the project
- Hard to generate changelogs automatically
- Doesn't indicate type of change (feature? docs? fix?)

### The Solution: Conventional Commits

Create `prompts/commit.md`:

```markdown
# Conventional Commits Helper

When the user wants to make a commit, help them create a properly formatted commit message.

## Format

\`\`\`
<type>[optional scope]: <description>
\`\`\`

## Types

- **feat**: New features
- **fix**: Bug fixes
- **docs**: Documentation changes
- **style**: Code style changes (formatting, etc.)
- **refactor**: Code refactoring without feature changes
- **test**: Adding or updating tests
- **chore**: Maintenance tasks (build, dependencies, etc.)

## Guidelines

- Use lowercase for type and description
- Keep description under 50 characters
- Use imperative mood: "add feature" not "added feature"
- Reference issue numbers when applicable

## Examples

- \`feat(quiz): add question filtering by topic\`
- \`fix(storage): resolve file encoding issue\`
- \`docs: update README with installation instructions\`
- \`test(quiz): add unit tests for get_next function\`
- \`refactor(storage): simplify file reading logic\`

Based on Conventional Commits specification from project standards.
```

### Using the Commit Prompt

From now on, when making commits:

1. Type: `>commit`
2. Your AI will help you format the commit message
3. Make the commit with the formatted message

Example:
```bash
git add prompts/commit.md
# Use >commit prompt to create message
git commit -m "feat(prompts): add conventional commits helper"
```

**What You've Learned:**
- ✅ Conventional commits format
- ✅ How prompts solve workflow problems
- ✅ Building your prompt infrastructure iteratively

## Phase 3: Build the Learning App

**Goal**: Implement the specification, one user story at a time.

### The Approach

Now you have:
- ✅ A specification (what to build)
- ✅ User stories (features to implement)
- ✅ A commit prompt (for clean history)

**Work with your AI to:**

1. **Pick the first user story** from your spec
2. **Discuss implementation approach** (How will you solve this?)
3. **Write the code** (Let your AI help, but you decide the approach)
4. **Test manually** (Run it, make sure it works)
5. **Commit using `>commit`** (Clean commit message)
6. **Move to next story**

### Example User Story: Add Questions

If your first story is: "As a learner, I want to add questions so I can study them later"

**Work with your AI:**
- Where should questions be stored? (Text file? JSON? CSV?)
- What information does each question need? (Topic, question text, answer)
- How should the interface work? (Command-line arguments? Interactive prompts?)

**Don't prescribe:** "Create add_question.py that takes sys.argv..."

**Instead:** "Let's implement the ability to add questions. What do you think is the best approach?"

### Iterate Through Stories

Continue implementing user stories until you have a working learning app.

**Use `>commit` for each story:**
```bash
>commit
# AI helps create: "feat(quiz): add ability to add new questions"
git commit -m "feat(quiz): add ability to add new questions"
```

**What You've Learned:**
- ✅ Spec-driven development
- ✅ Iterative implementation (one story at a time)
- ✅ Working collaboratively with AI
- ✅ Using your prompt infrastructure

## What's Next?

### You've Built

By completing this workshop, you now have:

1. **A working learning app** - Built following a proper spec
2. **Two reusable prompts**:
   - `>spec` - Create specifications and user stories
   - `>commit` - Format conventional commits

3. **Understanding of:**
   - Spec-driven development (requirements before code)
   - User stories (breaking down features)
   - Platform-agnostic tools (work with any AI)
   - Proper development workflow

### Using Your Prompts in Other Projects

These prompts aren't just for the learning app! Copy the `prompts/` directory to any project and use:

- `>spec` when starting new projects
- `>commit` for every commit

They work with any AI assistant because they're plain markdown.

### Next Workshop

**Workshop 2** will introduce **Agents** - prompt-commands that activate automatically based on context, rather than explicit invocation.

For example:
- Auto-format code when you edit files
- Suggest tests when you add new functions
- Check for security issues before commits

---

**Ready to build?** Start with Phase 1: Create the Specification.
