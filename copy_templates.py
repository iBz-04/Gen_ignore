import os
import shutil

# Create the templates directory if it doesn't exist
os.makedirs('gitignore_generator/templates', exist_ok=True)

# Copy the template files
shutil.copy('templates/python.txt', 'gitignore_generator/templates/')
shutil.copy('templates/javascript.txt', 'gitignore_generator/templates/')

print("Templates copied successfully!") 