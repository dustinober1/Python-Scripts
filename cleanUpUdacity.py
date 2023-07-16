import os

"""The code first specifies the folder path where the files are located. It then retrieves the list of files in that folder. For each file, it checks if the filename starts with "1. ", "2. ", "3. ", or ends with ", solution.ipynb". If a file matches any of these conditions, it removes the specified prefixes and/or suffix from the filename using the replace() method. Then, it creates the old and new file paths by joining the folder path with the respective filenames. Finally, it renames the file by moving it from the old path to the new path using the os.rename() function."""

folder_path = "/Users/dustinober/Downloads"

# Get the list of files in the folder
file_list = os.listdir(folder_path)

# Loop through the files
for filename in file_list:
    # Check if the file name starts with "1. ", "2. ", or ends with ", solutions"
    if filename.startswith("1. ") or filename.startswith("2. ") or filename.startswith("3. ") or filename.endswith(", solution.ipynb"):
        # Remove the prefixes and/or suffix
        new_filename = filename.replace("1. ", "").replace("2. ", "").replace("3. ", "").replace(", solution", ".ipynb")
        
        # Create the new file path
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_path, new_path)
