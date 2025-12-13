#!/usr/bin/env python3
"""
Prompt-command utility for platform-agnostic AI development.

This script implements the >name prompt-command convention by:
1. Looking up prompts in prompts/name.md or prompts/name/PROMPT.md
2. Reading and outputting prompt contents
3. Providing helpful error messages when prompts don't exist
4. Listing available prompts
5. Validating prompt structure

Usage:
    python prompt.py <name>           # Read and output a prompt
    python prompt.py --list           # List all available prompts
    python prompt.py --validate       # Validate all prompts
"""

import sys
import os
from pathlib import Path


def find_prompt(name):
    """
    Find and return the path to a prompt file.

    Checks for:
    1. prompts/name.md (simple prompt)
    2. prompts/name/PROMPT.md (complex prompt)

    Returns:
        Path object if found, None otherwise
    """
    simple_path = Path(f"prompts/{name}.md")
    if simple_path.exists():
        return simple_path

    complex_path = Path(f"prompts/{name}/PROMPT.md")
    if complex_path.exists():
        return complex_path

    return None


def read_prompt(name):
    """
    Read and return the contents of a prompt.

    Returns:
        Prompt contents as string, or error message
    """
    prompt_path = find_prompt(name)

    if prompt_path is None:
        available = list_prompts()
        if available:
            available_str = ", ".join(available)
            return f"Prompt '{name}' not found.\n\nAvailable prompts: {available_str}\n\nUse: python prompt.py --list to see all prompts"
        else:
            return f"Prompt '{name}' not found.\n\nNo prompts exist yet. Create one in prompts/{name}.md"

    try:
        with open(prompt_path, 'r') as f:
            contents = f.read()

        # Add metadata header
        prompt_type = "simple" if prompt_path.name == f"{name}.md" else "complex"
        header = f"# Prompt: {name} ({prompt_type})\n# Path: {prompt_path}\n\n"

        return header + contents
    except Exception as e:
        return f"Error reading prompt '{name}': {e}"


def list_prompts():
    """
    List all available prompts.

    Returns:
        List of prompt names
    """
    prompts = []
    prompts_dir = Path("prompts")

    if not prompts_dir.exists():
        return prompts

    # Find simple prompts (*.md files)
    for md_file in prompts_dir.glob("*.md"):
        prompts.append(md_file.stem)

    # Find complex prompts (directories with PROMPT.md)
    for item in prompts_dir.iterdir():
        if item.is_dir():
            prompt_file = item / "PROMPT.md"
            if prompt_file.exists():
                prompts.append(item.name)

    return sorted(prompts)


def validate_prompts():
    """
    Validate all prompts and report any issues.

    Returns:
        Validation report as string
    """
    prompts = list_prompts()

    if not prompts:
        return "No prompts found to validate."

    report = ["Validating prompts...\n"]
    issues = []

    for name in prompts:
        prompt_path = find_prompt(name)

        # Check if file is readable
        try:
            with open(prompt_path, 'r') as f:
                contents = f.read()

            # Check if file is empty
            if not contents.strip():
                issues.append(f"  ⚠ {name}: Prompt file is empty")
            else:
                report.append(f"  ✓ {name}: OK ({prompt_path})")

        except Exception as e:
            issues.append(f"  ✗ {name}: Error reading file - {e}")

    if issues:
        report.append("\nIssues found:")
        report.extend(issues)
    else:
        report.append("\nAll prompts valid!")

    return "\n".join(report)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python prompt.py <name>")
        print("       python prompt.py --list")
        print("       python prompt.py --validate")
        sys.exit(1)

    arg = sys.argv[1]

    if arg == "--list":
        prompts = list_prompts()
        if prompts:
            print("Available prompts:")
            for name in prompts:
                prompt_path = find_prompt(name)
                prompt_type = "simple" if prompt_path.name.endswith(f"{name}.md") else "complex"
                print(f"  - {name} ({prompt_type})")
        else:
            print("No prompts found.")
            print("\nCreate a prompt with:")
            print("  mkdir -p prompts")
            print("  echo 'Your instructions here' > prompts/example.md")
            print("  python prompt.py example")

    elif arg == "--validate":
        print(validate_prompts())

    else:
        # Read and output the prompt
        print(read_prompt(arg))


if __name__ == "__main__":
    main()
