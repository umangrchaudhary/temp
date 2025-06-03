# import os

# def load_stuff():
#   print(os.listdir())

import os

def show_files_and_directories(path=None):
    """Show files and directories in the given path."""
    if path is None:
        path = os.getcwd()  # Default to current directory if no path is provided

    if os.path.exists(path) and os.path.isdir(path):
        print(f"Files and directories in {path}:")
        for item in os.listdir(path):
            print(item)
    else:
        print(f"Error: {path} is not a valid directory.")


def show_file_content(file_path):
    """Print the content of the provided file."""
    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            print(f"Reading content of {file_path}:")
            print(file.read())  # Print the content of the file
    else:
        print(f"Error: {file_path} is not a valid file.")



def get_enx_variable(key):
    """Retrieve the environment variable value by key, or return the default value if not found."""
    return os.environ.get(key)

