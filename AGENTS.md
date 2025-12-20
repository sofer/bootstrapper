# Project Conventions

**READ THIS FILE AT THE START OF EVERY SESSION**

This file provides project conventions and session bootstrap instructions for AI coding assistants.

## Session Bootstrap

When this file is read at session start, you should:

### 1. Load All Skills

Read all skill descriptions from the `skills/` directory:

- Look for simple skills: `skills/*.md` files
- Look for complex skills: `skills/*/SKILL.md` files
- Extract the `name` and `description` from YAML frontmatter in each file
- Keep these descriptions in memory to match against user requests

**Skill frontmatter format:**
```yaml
---
name: skill-name
description: Brief description of when to use this skill
---
```

**How skills work:**
- Skills activate automatically when user requests match the description
- User doesn't need special syntax - just natural language
- When a skill is relevant, read the full skill file and follow its instructions
- Skills may reference supporting files in their directories

**Examples:**
- User: "I want to create a spec" → Match to spec skill → Read and follow skills/spec.md
- User: "commit these changes" → Match to commit skill → Read and follow skills/commit.md

### 2. Platform-Agnostic Mode

**CRITICAL: This template builds tools that work with ANY AI assistant.**

You MUST NOT use platform-specific features:

**Do Not Use or Suggest:**
- ❌ Vendor-specific APIs or features
- ❌ Built-in slash commands (like `/commit`, `/test`, `/review`)
- ❌ Platform-specific attribution footers in commits or code
- ❌ IDE-specific configuration or tools

**Use Instead:**
- ✅ Plain markdown files
- ✅ Standard Python scripts (or chosen language)
- ✅ Basic git commands
- ✅ Universal shell commands (POSIX-compliant)
- ✅ Natural language interaction

**Why this matters:**
- Skills created here work in Claude Code, Cursor, Aider, Codex CLI, Gemini CLI, and future tools
- Users learn transferable patterns, not vendor-specific tricks
- No lock-in to any single AI platform

### 3. First-Time Setup Check

Before checking project state, verify if this file has been configured:

- **Check for placeholder markers:** Look for `SETUP_PLACEHOLDER_RUNTIME`, `SETUP_PLACEHOLDER_LANGUAGE`, `SETUP_PLACEHOLDER_DOCS` in sections below
- **If ANY placeholder found:** Read SETUP.md and run interactive first-time configuration
- **If no placeholders found:** Configuration complete, skip to step 4

### 4. Check Project State

After loading skills and understanding conventions:

1. **Check `git log --oneline`** - See what's been completed
2. **Check `git status`** - Identify any uncommitted work
3. **List available skills** - Tell user what skills are loaded and ready

### 5. Confirm Ready

Let the user know you're ready:
- Skills loaded (list them)
- Project conventions understood
- Platform-agnostic mode enabled
- Ready to continue from current progress

---

## Architecture

### Runtime Environment

SETUP_PLACEHOLDER_RUNTIME

[After setup, this will describe whether the application runs within the AI coding interface or as a standalone application]

---

## Code Style

### General Principles

- Prefer functional style over object-oriented unless OOP clearly benefits the design
- Use descriptive variable and function names
- Keep functions small and focused (single responsibility)
- Comment only when logic isn't self-evident

### Programming Language

SETUP_PLACEHOLDER_LANGUAGE

[After setup, this will specify the programming language and language-specific conventions]

### Documentation

SETUP_PLACEHOLDER_DOCS

[After setup, this will specify the documentation standard: British English, American English, Simple English, or Technical/Formal]

- Be consistent with chosen standard throughout the project
- All skills, code comments, and documentation should follow this standard
- Write clear docstrings for non-obvious functions

---

## Testing

- Add testing as your project matures
- Framework choice will be documented after setup
- Focus on test-first workflow when applicable
- For Python: pytest with `-v` flag
- For JavaScript: Jest or framework of choice
- For other languages: choose appropriate testing framework

---

## Commits

Use **Conventional Commits** specification (https://www.conventionalcommits.org/):

**Format**: `<type>[optional scope]: <description>`

**Types**:
- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation changes
- `style`: Code style changes (formatting, missing semicolons, etc.)
- `refactor`: Code refactoring without feature changes
- `test`: Adding or updating tests
- `chore`: Maintenance tasks (build, dependencies, etc.)

**Examples**:
- `feat(quiz): add question filtering by topic`
- `fix(storage): resolve file encoding issue`
- `docs: update README with installation instructions`
- `test(quiz): add unit tests for get_next function`
- `refactor(storage): simplify file reading logic`

**Guidelines**:
- Use lowercase for type and description
- Keep description under 50 characters
- Use imperative mood: "add feature" not "added feature"
- Reference issue numbers when applicable: `feat(auth): add login (#123)`
- **Do not add attribution footers** (no "Generated with..." or "Co-Authored-By: AI")

---

## Skills

Skills are reusable AI capabilities stored as markdown files in the `skills/` directory.

### Skill Structure

Each skill is a markdown file with YAML frontmatter:

```yaml
---
name: skill-name
description: Brief description of when to use this skill. AI uses this to decide when to activate automatically.
---

# Skill Name

[Instructions for what the skill does]
```

### Creating New Skills

When creating skills:
- **Simple skills**: Single `.md` file in `skills/` directory
- **Complex skills**: Directory `skills/name/` with `SKILL.md` plus supporting files
- Use clear, descriptive names
- Write descriptions that help AI understand when to activate the skill
- Focus on reusable capabilities, not one-time tasks

### Available Skills

See `skills/` directory for currently available skills. Skills are loaded at session start (see Session Bootstrap section above).

---

## Workflow

### Spec-First Development

1. Start with problem statement
2. Create specification (what the system does)
3. Define user stories (features from user perspective)
4. Implement iteratively, one story at a time
5. Use conventional commits for clean history

### User Stories Format

```
As a [user type], I want [goal] so that [benefit]
```

Create checkbox lists for tracking:
- [ ] User story description

---

## Platform Agnostic Principles

This template creates skills and tools that work with any AI coding assistant:

- ✅ Claude Code
- ✅ Cursor
- ✅ Aider
- ✅ Codex CLI (OpenAI)
- ✅ Gemini CLI (Google)
- ✅ ChatGPT
- ✅ Any future AI coding assistant

**How:** Skills and AGENTS.md are plain markdown. Standard git commands. Universal shell scripts. Natural language interaction.

**Goal:** No vendor lock-in. Transferable skills across all AI tools.
