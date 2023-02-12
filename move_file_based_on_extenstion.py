import os
import shutil

# Define the source and destination directories
src_dir = "/Users/dustinober/Downloads"
dst_dir = "/Users/Shared/fonts"

# Recursively loop through all subdirectories in the source directory
for root, dirs, files in os.walk(src_dir):
    # Loop through each file in the current directory
    for file in files:
        # Check if the file has the .tff extension
        if file.endswith(".ttf") or file.endswith(".TTF"):
            # Get the full path of the file
            src_path = os.path.join(root, file)

            # Move the file to the destination directory
            dst_path = os.path.join(dst_dir, file)
            shutil.move(src_path, dst_path)
