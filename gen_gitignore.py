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
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, "templates", f"{language}.txt")
    
    try:
        with open(template_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Template file for {language} not found.")
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