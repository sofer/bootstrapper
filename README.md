# Workshop 1: Introduction to Prompt-Commands

**Learn to build AI-agnostic development tools by creating a quiz app, then improving it with prompt infrastructure**

## Prerequisites

Before starting this workshop, you should have:

- **Python installed** (version 3.8 or later)
- **Git basics** (clone, commit, branch)
- **Basic command-line knowledge**
- **An AI coding assistant** (Claude Code, Aider, Cursor, etc.)

### Documentation Standard: British English

Throughout this workshop, we'll use **British English** for all documentation, comments, and user-facing text. This includes:

- British spellings: "organise" not "organize", "colour" not "color"
- British terminology: "whilst" not "while", "amongst" not "among"
- Consistent voice: Clear and accessible to both technical and non-technical readers

This is a simple convention that ensures consistency across projects and teams.

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
- Example: `>quiz` to start your quiz session

### How They Work

1. You create a prompt file: `prompts/commit.md`
2. You invoke it in conversation: `>commit`
3. Your AI reads the file and follows the instructions
4. It works everywhere because it's just markdown

### Why Use Prompt-Commands?

- **Portable**: Take your tools to any AI platform
- **Inspectable**: See exactly what instructions the AI follows
- **Customisable**: Edit the markdown files to change behaviour
- **Shareable**: Team members can use the same prompts
- **Versioned**: Store in git like any code
- **No lock-in**: Not dependent on any single AI vendor

## Workshop Overview

This workshop uses a **"build simply, then improve"** approach:

1. **Phase 1**: Build a basic quiz app (no best practices yet)
2. **Phases 2-5**: Add prompt infrastructure to solve real problems
3. **Learn by doing**: See the value of each prompt as you add it

By the end, you'll have:
- A working spaced repetition quiz tool
- Four reusable prompt-commands (`>spec`, `>test`, `>commit`, `>pr`)
- Understanding of how to build AI-agnostic development tools

## Phase 1: Build Minimum Viable Quiz

**Goal**: Create a working quiz app without worrying about best practices yet.

### What We're Building

A simple quiz tool that:
- Lets you add questions with topics
- Retrieves questions to ask
- Records your answers
- Stores everything in a simple text file

### Implementation

Create three basic Python scripts in `scripts/`:

1. **`add_question.py`** - Append questions to `data/questions.txt`
   - Takes input: topic, question, answer
   - Appends to file in simple format

2. **`get_next.py`** - Read and return next question from file
   - Reads from `data/questions.txt`
   - Returns first unasked question

3. **`record_answer.py`** - Append answer to `data/questions.txt`
   - Records user's answer
   - Marks question as answered

### Directory Structure

```
scripts/
├── add_question.py
├── get_next.py
└── record_answer.py
data/
└── questions.txt
```

### Getting Started

1. Create the directories:
   ```bash
   mkdir -p scripts data
   ```

2. Build the three Python scripts (keep them simple!)

3. Test manually:
   ```bash
   python scripts/add_question.py
   python scripts/get_next.py
   python scripts/record_answer.py
   ```

4. Make git commits as you go:
   ```bash
   git add scripts/add_question.py
   git commit -m "add question script"
   ```

**Note**: Don't worry about perfect commit messages yet - we'll improve this in Phase 4!

### What's Missing?

At this stage, we have:
- ✅ Working code
- ❌ No formal specification
- ❌ No tests
- ❌ Inconsistent commit messages
- ❌ No collaboration workflow

This is intentional! We'll add these using prompts in the next phases.

## Phase 2: Add Spec Infrastructure

**Goal**: Create a `>spec` prompt that helps document what we've built.

### The Problem

We built working code, but there's no clear documentation of:
- What the quiz app does
- What features it should have
- What user stories it fulfils

### The Solution: `>spec` Prompt

Create `prompts/spec.md` based on the CLAUDE.md template:

```markdown
# Specification Writer

When the user asks to create or update a specification, help them:

1. **Project Specification**
   - High-level project goals
   - What problem does it solve?
   - Who is it for?

2. **User Stories**
   - Format: "As a [user type], I want [goal] so that [benefit]"
   - Create checkbox list for tracking
   - Example: "- [ ] As a student, I want to add questions so that I can study later"

3. **Architecture & Technical Notes**
   - How does it work?
   - What files are involved?
   - Any important design decisions

Use British English for all documentation.

Based on README Structure Template from project standards.
```

### Using the Prompt

1. In conversation with your AI: `>spec`
2. AI reads the prompt and helps you create a specification
3. Add the spec to your README or a separate `SPEC.md` file
4. Make a commit:
   ```bash
   git add prompts/spec.md README.md
   git commit -m "add spec prompt and project specification"
   ```

### Value Demonstrated

✅ **Proper documentation** - Clear record of what the project does
✅ **Reusable tool** - Use `>spec` in future projects
✅ **Team communication** - Others can understand the project quickly

## Phase 3: Add Testing Infrastructure

**Goal**: Create a `>test` prompt that guides Test-Driven Development.

### The Problem

How do we know if our code works? What if we make changes and break something?

### The Solution: `>test` Prompt + pytest

1. **Create `prompts/test.md`**:

```markdown
# Test-Driven Development Guide

When the user wants to test code, guide them through TDD workflow:

## TDD Process

1. **Write a failing test first**
   - Define expected behaviour
   - Test should fail (red)

2. **Run the failing test**
   - Confirm it fails as expected
   - `pytest -v` for line-by-line output

3. **Write minimal code to make it pass**
   - Just enough to turn the test green
   - No extra features

4. **Run the passing test**
   - Confirm it passes (green)
   - All tests should pass

5. **Refactor if needed**
   - Clean up code
   - Maintain test coverage

6. **Run tests again**
   - Ensure refactoring didn't break anything

## Testing Principles

- Test edge cases and error conditions
- Clear test names that read like documentation
- One test per behaviour
- Fast, independent tests

Use pytest for testing Python code.

Based on TDD workflow from project standards.
```

2. **Install pytest**:
   ```bash
   pip install pytest
   ```

3. **Create `tests/` directory**:
   ```bash
   mkdir tests
   ```

4. **Use `>test` to add tests**:
   - In conversation: `>test`
   - AI guides you through writing tests for existing scripts
   - Run: `pytest -v` to see line-by-line pass/fail

### Example Test

```python
# tests/test_add_question.py
def test_add_question_creates_file():
    # Test that add_question creates data file
    # ...
```

### Value Demonstrated

✅ **Confidence in changes** - Know when something breaks
✅ **Better design** - Writing tests reveals design issues
✅ **Documentation** - Tests show how code should work
✅ **Reusable process** - Use `>test` for all future code

## Phase 4: Add Commit Infrastructure

**Goal**: Create a `>commit` prompt for consistent commit messages.

### The Problem

Looking at our git history, we see inconsistent commit messages:
- "add question script"
- "fixed bug"
- "updates"

These don't follow any standard and aren't very informative.

### The Solution: `>commit` Prompt + Conventional Commits

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

### Using the Prompt

1. In conversation: `>commit`
2. AI helps you create a properly formatted commit message
3. Make the commit:
   ```bash
   git add .
   git commit -m "feat(test): add test infrastructure with pytest"
   ```

### Value Demonstrated

✅ **Clear history** - Understand what changed and why
✅ **Automated tools** - Conventional commits enable changelog generation
✅ **Team standards** - Everyone commits the same way
✅ **Future reference** - Easy to find specific types of changes

## Phase 5: Add PR Infrastructure (Optional)

**Goal**: Create a `>pr` prompt for streamlined pull requests.

### The Problem

Creating pull requests involves:
- Writing a summary of changes
- Describing what was tested
- Linking to relevant issues or user stories

This is repetitive and easy to forget steps.

### The Solution: `>pr` Prompt

Create `prompts/pr.md`:

```markdown
# Pull Request Creator

When the user wants to create a pull request, help them:

1. **Review changes**
   - Run: \`git diff main...HEAD\`
   - Summarise what changed

2. **Create PR title**
   - Follow conventional commit format
   - Be descriptive but concise

3. **Write PR body**
   - Summary of changes (bullet points)
   - What was tested
   - Link to user stories or issues

4. **Create the PR**
   - Use: \`gh pr create --title "..." --body "..."\`
   - Include summary and test plan

## Template

\`\`\`markdown
## Summary
- Added X feature
- Fixed Y bug
- Updated Z documentation

## Testing
- [ ] Unit tests pass (\`pytest -v\`)
- [ ] Manual testing completed
- [ ] Documentation updated

## Related
- Closes #issue-number
- Implements user story: ...
\`\`\`

Based on PR process from project standards.
```

### Value Demonstrated

✅ **Complete PRs** - Never forget important details
✅ **Faster reviews** - Reviewers have all context
✅ **Consistent format** - All PRs look the same
✅ **Reusable across projects** - Same prompt works everywhere

## What's Next?

### You've Built

By completing this workshop, you now have:

1. **A working quiz tool** - With spaced repetition and topic filtering
2. **Four reusable prompts**:
   - `>spec` - Create specifications and user stories
   - `>test` - Guide TDD workflow
   - `>commit` - Format conventional commits
   - `>pr` - Create pull requests

3. **Understanding of prompt-commands**:
   - How to create them
   - When to use them
   - Why they're valuable

### Using Your Prompts in Other Projects

These prompts aren't just for the quiz app! Copy the `prompts/` directory to any project and use:

- `>spec` when starting new projects
- `>test` when writing any code
- `>commit` for every commit
- `>pr` for every pull request

They work with any AI assistant because they're plain markdown.

### Next Workshop

**Workshop 2** will introduce **Actors** - prompt-commands that activate automatically based on context, rather than explicit invocation.

For example:
- Auto-format code when you edit files
- Suggest tests when you add new functions
- Check for security issues before commits

---

**Ready to build?** Start with Phase 1 and create your minimum viable quiz app!
