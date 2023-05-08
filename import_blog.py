import os
import shutil
import argparse
import frontmatter

# Set up command line argument parser
parser = argparse.ArgumentParser(description="Move and rename index.md files in the pages directory.")
parser.add_argument("root_directory", type=str, help="Path to the root directory.")
parser.add_argument("destination_directory", type=str, help="Path to the destination directory.")
args = parser.parse_args()

# Define a function to move index.md files and rename them
def move_index_files(root_directory, destination_directory):
    # Loop through all directories in the root directory
    for directory in os.listdir(root_directory):
        # Check if the current item is a directory
        if os.path.isdir(os.path.join(root_directory, directory)):
            # Check if the directory contains an "index.md" file
            index_file = os.path.join(root_directory, directory, "index.md")
            if os.path.isfile(index_file):
                # Determine the new filename based on the directory name
                new_filename = f"{directory}.md"

                # Copy and rename the file to the destination directory
                destination_file = os.path.join(destination_directory, new_filename)
                shutil.copy2(index_file, destination_file)

                # Update the frontmatter in the new file
                update_frontmatter(destination_file)

# Define a function to update the frontmatter section of a Markdown file
def update_frontmatter(file_path):
    with open(file_path) as file:
        content = file.read()
        post = frontmatter.loads(content)

    if 'date' in post.keys():
        post['pubDate'] = post.metadata.pop('date')

    with open(file_path, 'w') as file:
        file.write(frontmatter.dumps(post))

# Call the function with command line arguments
move_index_files(args.root_directory, args.destination_directory)
