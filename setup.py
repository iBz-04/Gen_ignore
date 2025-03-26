# This file is intentionally left empty. 

from setuptools import setup, find_packages

setup(
    name="gitignore-generator",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    data_files=[('templates', ['templates/python.txt', 'templates/javascript.txt'])],
    entry_points={
        "console_scripts": [
            "gen-gitignore=gitignore_generator:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool to generate gitignore files for different languages",
    keywords="git, gitignore, cli",
    python_requires=">=3.6",
) 