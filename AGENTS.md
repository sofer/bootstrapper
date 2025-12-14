# Project Conventions

This file defines conventions for the bootstrapper workshop project, following the emerging AGENTS.md standard for AI coding assistants.

## Code Style

### Python
- Use Python 3.8+ features
- Follow PEP 8 style guidelines
- Prefer functional style over object-oriented unless OOP clearly benefits the design
- Use descriptive variable and function names
- Keep functions small and focused (single responsibility)

### Documentation
- **Documentation Standard**: [Not yet specified - choose British English, American English, Simple English, Technical, etc.]
- Be consistent with chosen standard throughout the project
- All skills, code comments, and documentation should follow this standard
- Write clear docstrings for non-obvious functions
- Comment only when logic isn't self-evident

## Testing

- Not included in Workshop 1
- Will be introduced in later workshops
- When introduced: pytest with `-v` flag for verbose output

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
- Do not add attribution footers (no "Generated with..." or "Co-Authored-By: AI")

## Skills

Skills are reusable AI capabilities stored as markdown files in the `skills/` directory.

### Available Skills

See `skills/` directory for currently available skills. Skills are loaded at session start via INIT.md.

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

## Platform Agnostic Principles

This workshop teaches platform-agnostic AI development:

- ❌ **Avoid**: Vendor-specific APIs, built-in slash commands, platform-specific features
- ✅ **Use**: Plain markdown files, standard Python, basic git commands, universal shell scripts
- ✅ **Goal**: Skills that work with any AI assistant (Claude Code, Cursor, Aider, Codex CLI, Gemini CLI, etc.)

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

## File Structure

```
project/
├── INIT.md              # Session bootstrap (read at start)
├── AGENTS.md            # This file - project conventions
├── README.md            # Workshop instructions
├── ARCHITECTURE.md      # Technical architecture reference
├── skills/              # Reusable AI capabilities
│   ├── spec.md         # Pre-built: specification creator
│   ├── commit.md       # Pre-built: commit message formatter
│   └── quiz.md         # User builds this in workshop
└── [project files]      # Learning app implementation
```

## Session Initialization

At the start of each session, the user should say:

> "Read INIT.md"

This ensures:
1. All skill descriptions are loaded
2. This AGENTS.md file is read for conventions
3. Platform-agnostic rules are established
4. AI is ready to assist with the project
