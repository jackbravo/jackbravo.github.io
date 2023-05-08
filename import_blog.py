import os
import shutil

# Specify the path to the directory containing the "pages" folder
root_directory = "/path/to/root/directory"

# Define a function to move index.md files and rename them
def move_index_files(root_directory):
    # Navigate to the "pages" folder
    pages_directory = os.path.join(root_directory, "pages")
    os.chdir(pages_directory)
    
    # Loop through all directories in the "pages" folder
    for directory in os.listdir():
        # Check if the current item is a directory
        if os.path.isdir(directory):
            # Check if the directory contains an "index.md" file
            index_file = os.path.join(directory, "index.md")
            if os.path.isfile(index_file):
                # Determine the new filename based on the directory name
                new_filename = f"{directory}.md"
                
                # Move and rename the file
                destination_file = os.path.join(root_directory, new_filename)
                shutil.move(index_file, destination_file)

# Call the function
move_index_files(root_directory)
