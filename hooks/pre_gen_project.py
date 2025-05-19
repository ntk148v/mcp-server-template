"""Pre-generation hook for cookiecutter."""
import os
import shutil


def main():
    """Main function."""
    # List of directories to exclude from template processing
    exclude_dirs = ['.venv', 'venv', '__pycache__']

    # Get the current directory
    project_dir = os.getcwd()

    # Remove any existing virtual environment directories
    for exclude_dir in exclude_dirs:
        dir_path = os.path.join(project_dir, exclude_dir)
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)

if __name__ == '__main__':
    main()
