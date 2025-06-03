# import os

# def load_stuff():
#   print(os.listdir())


import os

def load_stuff(directory=None):
    """List the files in a directory. If no directory is provided, list files in the current directory."""
    if directory is None:
        directory = os.getcwd()  # Default to the current working directory if no directory is provided

    # Check if the provided directory exists
    if os.path.exists(directory) and os.path.isdir(directory):
        print(f"Files and directories in {directory}:")
        for item in os.listdir(directory):
            print(item)
    else:
        print(f"Error: {directory} is not a valid directory.")

def print_file_content(file_path):
    """Print the content of a file if it exists."""
    if os.path.exists(file_path) and os.path.isfile(file_path):
        try:
            with open(file_path, 'r') as file:
                print(f"Content of {file_path}:")
                print(file.read())  # Print the content of the file
        except Exception as e:
            print(f"Error reading the file: {e}")
    else:
        print(f"Error: {file_path} is not a valid file.")
