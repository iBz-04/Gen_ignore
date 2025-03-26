# Gitignore Generator

A simple CLI tool to generate `.gitignore` files for different programming languages.

## Installation

```bash

pip install gitignore-generator==0.1.0 

```

## Usage

Run the command in your project root:

```bash
gen-gitignore
```

The tool will:

1. Ask you to select a language (Python or JavaScript/TypeScript)
2. Generate a `.gitignore` file with standard patterns for the selected language
3. If a `.gitignore` already exists, you'll be asked to overwrite or merge

## Features

- Language selection (Python, JavaScript/TypeScript)
- Standard gitignore patterns for each language
- Safe handling of existing gitignore files (overwrite or merge)

## License

MIT 