import os
import shutil
import argparse

# Set up command line argument parser
parser = argparse.ArgumentParser(description="Move and rename index.md files in the pages directory.")
parser.add_argument("root_directory", type=str, help="Path to the root directory.")
parser.add_argument("destination_directory", type=str, help="Path to the destination directory.")
args = parser.parse_args()

# Define a function to move index.md files and rename them
def move_index_files(root_directory, destination_directory):
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

                # Move and rename the file to the destination directory
                source_file = os.path.join(pages_directory, index_file)
                destination_file = os.path.join(destination_directory, new_filename)
                shutil.move(source_file, destination_file)

# Call the function with command line arguments
move_index_files(args.root_directory, args.destination_directory)
