from setuptools import setup, find_packages
import os

# Read the long description from README.md, or use a fallback if file not found
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A CLI tool to generate gitignore files for different languages"

setup(
    name="gitignore-generator",
    version="0.1.1",
    packages=find_packages(),
    include_package_data=True,
    data_files=[('templates', ['templates/python.txt', 'templates/javascript.txt'])],
    entry_points={
        "console_scripts": [
            "gen-gitignore=gitignore_generator:main",
        ],
    },
    author="Ibrahim Rayamah",
    author_email="issakaibrahimrayamah@gmail.com",
    description="A CLI tool to generate gitignore files for different languages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iBz-04/Gen_ignore",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="git, gitignore, cli",
    python_requires=">=3.6",
) 