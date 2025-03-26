#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def select_language():
    """Prompt user to select a language for gitignore template."""
    print("Select a language for your .gitignore:")
    print("1. Python")
    print("2. JavaScript/TypeScript")
    
    while True:
        choice = input("Enter choice (1/2): ").strip()
        if choice == "1":
            return "python"
        elif choice == "2":
            return "javascript"
        else:
            print("Invalid choice. Please enter 1 or 2.")

def get_template_content(language):
    """Read the template file for the selected language."""
    # Try multiple locations for the template file
    possible_paths = [
        # Try direct path from package
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", f"{language}.txt"),
        # Try from current working directory
        os.path.join(os.getcwd(), "templates", f"{language}.txt"),
        # Try from package directory
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates", f"{language}.txt")
    ]
    
    for template_path in possible_paths:
        if os.path.exists(template_path):
            try:
                with open(template_path, 'r') as f:
                    return f.read()
            except Exception as e:
                continue

    # If no template was found, use hardcoded templates as fallback
    print(f"Warning: Could not find {language}.txt template file.")
    print("Using built-in template instead.")
    
    if language == "python":
        return """# Python gitignore template

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
dist/
build/
*.egg-info/

# Virtual environments
venv/
env/
ENV/

# IDE specific files
.idea/
.vscode/
*.swp
*.swo

# Jupyter Notebook
.ipynb_checkpoints

# Testing
.coverage
htmlcov/
"""
    elif language == "javascript":
        return """# JavaScript/TypeScript gitignore template

# Dependencies
node_modules/
bower_components/

# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Build output
dist/
build/
out/

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE specific files
.idea/
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
"""
    else:
        print(f"Error: No built-in template for {language}.")
        sys.exit(1)

def handle_existing_gitignore(template_content):
    """Handle the case when .gitignore already exists."""
    if os.path.exists('.gitignore'):
        print(".gitignore already exists.")
        choice = input("Do you want to (o)verwrite or (m)erge? ").strip().lower()
        
        if choice == 'o':
            write_gitignore(template_content)
            print(".gitignore overwritten successfully.")
        elif choice == 'm':
            try:
                with open('.gitignore', 'r') as f:
                    current_content = f.read()
                
                # Simple merge strategy: add new content at the end with a separator
                merged_content = current_content.strip() + "\n\n# Added by gitignore-generator\n" + template_content
                write_gitignore(merged_content)
                print(".gitignore merged successfully.")
            except Exception as e:
                print(f"Error merging .gitignore: {e}")
                sys.exit(1)
        else:
            print("Invalid choice. Exiting without changes.")
            sys.exit(0)
    else:
        write_gitignore(template_content)
        print(".gitignore created successfully.")

def write_gitignore(content):
    """Write content to .gitignore file."""
    try:
        with open('.gitignore', 'w') as f:
            f.write(content)
    except Exception as e:
        print(f"Error writing .gitignore: {e}")
        sys.exit(1)

def main():
    """Main function to generate .gitignore file."""
    print("Gitignore Generator")
    print("-------------------")
    
    language = select_language()
    template_content = get_template_content(language)
    handle_existing_gitignore(template_content)

if __name__ == "__main__":
    main() 