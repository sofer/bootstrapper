---
name: spec
description: Create or update project specifications with user stories. Use when user wants to plan a project, create a spec, or define requirements.
---

# Specification Writer

When the user asks to create or update a specification, help them create a spec and save it to `SPEC.md`:

## 1. Project Specification

Start with high-level goals:
- What problem does this project solve?
- Who is it for?
- What are the main objectives?

## 2. User Stories

Create user stories in the format:
```
As a [user type], I want [goal] so that [benefit]
```

Format as checkbox list for tracking:
```
- [ ] As a learner, I want to add questions so that I can study them later
- [ ] As a learner, I want to test myself so that I can practice recall
```

Guidelines:
- Keep stories small and implementable
- Each story should be independently valuable
- Focus on user perspective, not implementation details
- Order stories by priority (most important first)

## 3. Architecture & Technical Notes

Document high-level technical approach:
- How does the system work (conceptually)?
- What are the key components?
- What are important design decisions?
- What technologies or approaches will be used?

Keep this high-level - avoid over-specifying implementation details that should be decided during development.

## 4. Documentation Standard

Follow the project's chosen documentation standard for all text (check README.md or ask user for their preference if not yet specified).

## 5. Save the Specification

Save the completed specification to `SPEC.md` in the project root.

## Example Structure

```markdown
# [Project Name]

## Project Specification

[High-level description of what the project does and why it exists]

## User Stories

- [ ] As a [user], I want [goal] so that [benefit]
- [ ] As a [user], I want [goal] so that [benefit]
- [ ] As a [user], I want [goal] so that [benefit]

## Architecture & Technical Notes

[Technical approach and key design decisions]
```

## Notes

This skill is based on spec-driven development principles:
- Define requirements before implementation
- Use user stories to break down features
- Document architecture decisions early
- Create a contract between planning and development

The resulting SPEC.md serves as the guiding document for development.
