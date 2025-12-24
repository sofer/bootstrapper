# First-Time Setup Guide

**This file is only read during first-time template configuration.**

When an AI assistant detects SETUP_PLACEHOLDER markers in AGENTS.md, it should read this file and follow these instructions to configure the project.

## Overview

This automated setup process asks the user 5 questions and updates AGENTS.md and README.md with project-specific configuration.

## When Setup Triggers

Setup triggers when AGENTS.md contains these placeholder markers:
- `SETUP_PLACEHOLDER_RUNTIME` (Runtime Environment section)
- `SETUP_PLACEHOLDER_LANGUAGE` (Programming Language section)
- `SETUP_PLACEHOLDER_DOCS` (Documentation Standard section)

If all three are found, begin interactive configuration.

## Question Flow

Ask questions conversationally, one at a time. Don't rush or present all questions at once.

### Question 1: Project Name
**Ask:** "What's the name of your project?"
**Format:** Free text
**Examples:** "task-manager", "CodeQuiz", "API Gateway"
**Store as:** `PROJECT_NAME`

### Question 2: Project Description
**Ask:** "In one sentence, what does this project do?"
**Format:** Free text, ideally 10-20 words
**Example:** "A CLI tool for managing daily tasks with natural language input"
**Store as:** `PROJECT_DESCRIPTION`

### Question 3: Runtime Environment
**Ask:** "Will this project run:"
- "1. Within the AI coding interface (AI is the interface, no separate deployment)"
- "2. As a standalone application (traditional deployment with separate UI)"

**Format:** User chooses 1 or 2
**Store as:** `RUNTIME_CHOICE` (1 or 2)

### Question 4: Programming Language
**Ask:** "What programming language will you use? (e.g., Python, JavaScript, Go, TypeScript)"
**Format:** Free text
**Examples:** "Python", "JavaScript", "TypeScript", "Go", "Rust"
**Store as:** `LANGUAGE`

**Follow-up ask:** "Any language-specific conventions to note? (press Enter to skip)"
**Format:** Free text, optional
**Examples:** "Use async/await for all I/O", "Prefer functional programming", "Follow PEP 8 strictly"
**Store as:** `LANGUAGE_CONVENTIONS` (can be empty)

### Question 5: Documentation Standard
**Ask:** "What documentation standard should we use?"
- "1. British English"
- "2. American English"
- "3. Simple English"
- "4. Technical/Formal"

**Format:** User chooses 1-4
**Store as:** `DOC_STANDARD` (1, 2, 3, or 4)

### Confirmation

After all questions, show summary:

```
Here's your project configuration:
- Project Name: {PROJECT_NAME}
- Description: {PROJECT_DESCRIPTION}
- Runtime: {runtime choice description}
- Language: {LANGUAGE}
- Conventions: {LANGUAGE_CONVENTIONS or "None specified"}
- Documentation: {doc standard description}

Does this look correct? (yes/no)
```

If "no": Ask "Which would you like to change?" and allow re-answering specific questions.
If "yes": Proceed to file updates.

## File Updates

### Update 1: AGENTS.md Runtime Environment Section

**Find:** `SETUP_PLACEHOLDER_RUNTIME`

**Replace with (if RUNTIME_CHOICE = 1):**
```markdown
This application runs within the AI coding interface:
- Application runs via natural language interaction with AI assistant
- AI assistant is the interface
- No API keys or separate deployment needed
- Skills provide capabilities
- Simple file-based storage (JSON, CSV, etc.)
```

**Replace with (if RUNTIME_CHOICE = 2):**
```markdown
This application runs as a standalone application:
- Traditional approach with separate deployment
- Own UI (GUI or CLI)
- May require LLM API access if AI features needed
- Standard runtime environment
```

### Update 2: AGENTS.md Programming Language Section

**Find:** `SETUP_PLACEHOLDER_LANGUAGE`

**Replace with language-specific content:**

**For Python:**
```markdown
**Language:** Python 3.8+
- Follow PEP 8 style guidelines
- Use type hints where beneficial
{LANGUAGE_CONVENTIONS if provided}
```

**For JavaScript:**
```markdown
**Language:** JavaScript (ES6+)
- Follow Standard JS style guide
- Prefer const/let over var
- Use async/await for async operations
{LANGUAGE_CONVENTIONS if provided}
```

**For TypeScript:**
```markdown
**Language:** TypeScript
- Use strict mode
- Define interfaces for all data structures
- Prefer explicit types over implicit
{LANGUAGE_CONVENTIONS if provided}
```

**For Go:**
```markdown
**Language:** Go
- Follow Effective Go guidelines
- Use gofmt for formatting
- Keep packages focused and small
{LANGUAGE_CONVENTIONS if provided}
```

**For other languages:**
Provide sensible defaults based on the language name and add LANGUAGE_CONVENTIONS if provided.

### Update 3: AGENTS.md Documentation Standard

**Find:** `SETUP_PLACEHOLDER_DOCS`

**Replace with:**
```markdown
**Documentation Standard:** {chosen standard name}
- Be consistent throughout the project
- All skills, code comments, and documentation follow this standard
```

Where choices map to:
- 1 → "British English"
- 2 → "American English"
- 3 → "Simple English"
- 4 → "Technical/Formal"

### Update 4: Transform README.md

**Replace entire README.md content** with project-specific documentation.

**New README.md structure:**

```markdown
# {PROJECT_NAME}

{PROJECT_DESCRIPTION}

## Architecture

### Runtime Environment

{Expanded runtime description based on RUNTIME_CHOICE:
  - If RUNTIME_CHOICE = 1: "This application runs within the AI coding interface. You interact with it via natural language with your AI assistant. No separate deployment or API keys needed. Skills provide the application's capabilities."
  - If RUNTIME_CHOICE = 2: "This application runs as a standalone application with traditional deployment. It has its own UI and standard runtime environment."
}

### Technical Stack

- **Language**: {LANGUAGE}
- **Documentation**: {DOC_STANDARD name}
- **Commits**: Conventional Commits specification
- **Skills**: AI capabilities via skills directory

## Project Structure

    ```
    project/
    ├── .claude/
    │   ├── skills -> ../skills  # Symlink for Claude Code compatibility
    │   └── settings.local.json  # Claude-specific settings (not tracked)
    ├── AGENTS.md                # Project conventions and session bootstrap
    ├── README.md                # This file - project documentation
    ├── CLAUDE.md                # Claude Code auto-load redirect
    ├── GEMINI.md                # Gemini CLI redirect (future compatibility)
    ├── SETUP.md                 # First-time setup guide (for AI assistants)
    ├── skills/                  # Canonical location for AI capabilities
    │   ├── spec.md             # Creates project specifications
    │   └── commit.md           # Formats commit messages
    └── [project files]          # Your application code
    ```

## Getting Started

### For AI Coding Assistants

To start working with this project:

**Codex CLI (OpenAI):** AGENTS.md loads automatically - just start working

**Claude Code:** Say anything to start (if CLAUDE.md is configured), or say "Read AGENTS.md"

### What Happens at Session Start

When AGENTS.md is loaded, your AI assistant will:
1. Load all available skills from the `skills/` directory
2. Check your current progress via git
3. Report available skills and conventions
4. Get ready to help

### Available Skills

Current skills in `skills/` directory:
- **spec** - Create project specifications
- **commit** - Format commit messages following Conventional Commits

To add more skills, create `skills/skillname.md` with YAML frontmatter and instructions.

## Development Workflow

### Spec-First Development

1. Start with problem statement
2. Create specification (what the system does)
3. Define user stories (features from user perspective)
4. Implement iteratively, one story at a time
5. Use conventional commits for clean history

### Using Skills

You don't need special syntax. Just talk naturally:

- "Create a spec for a quiz app" → AI activates spec skill
- "I want to commit these changes" → AI activates commit skill
- "Run the tests" → AI activates test skill (if you've added one)

The AI automatically matches your request to the appropriate skill based on descriptions.

### Creating Skills

Skills are markdown files with YAML frontmatter:

```yaml
---
name: skill-name
description: When to use this skill. AI uses this to auto-activate.
---

# Skill Name

[Instructions for what the skill does]
```

**Simple skills:** Single `.md` file in `skills/` directory
**Complex skills:** Directory `skills/name/` with `SKILL.md` plus supporting files

## Session Resume

Since conversations may be interrupted:
- Git tracks completed work
- AGENTS.md reloads all context
- AI checks git log to see progress
- Continue from where you left off

Just say "Read AGENTS.md" again to re-establish context in a new session.

## References

- [Introducing Agent Skills | Anthropic](https://www.anthropic.com/news/skills)
- [Agent Skills Documentation | Claude](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

For detailed conventions, coding standards, and session bootstrap process, see AGENTS.md.
```

### Completion Message

After all files are updated, show:

```
Configuration complete! Here's what was set up:

Project Configuration:
- Name: {PROJECT_NAME}
- Description: {PROJECT_DESCRIPTION}
- Runtime: {runtime choice description}
- Language: {LANGUAGE}
- Documentation: {doc standard name}

Updated Files:
- AGENTS.md (configured with your project settings)
- README.md (transformed to project documentation)

Next Steps:
1. Review the changes to AGENTS.md and README.md
2. When ready, say "commit these changes" to create a commit
3. Suggested commit message: "chore: configure project from template"
```

Then continue with normal session bootstrap (check git status, list skills, confirm ready).

## Edge Cases

### User interrupts setup
- Don't modify any files
- Next session will detect placeholders and restart setup

### User provides unclear answer
- Ask for clarification
- Provide examples of good answers
- Re-ask the question

### User wants to change answer after confirmation
- Show numbered list of all answers
- Ask which number to change
- Re-ask that specific question
- Show updated summary and confirm again

### File write fails
- Report error clearly with filename
- Don't continue to next file
- Don't proceed with bootstrap
- User can retry setup next session

### User doesn't know what to answer
- Provide context and examples for the question
- Suggest common choices
- Allow "skip for now" only if truly optional (language conventions)

## Notes

This setup process is designed to be:
- **Conversational** - One question at a time, natural flow
- **Clear** - Examples and context for each question
- **Flexible** - Allow changes before committing
- **Robust** - Handle errors gracefully
- **Minimal** - Just 5 questions to configure the essentials

The AI assistant should feel empowered to adapt this flow slightly to the user's responses while maintaining the core structure and ensuring all required information is collected.
