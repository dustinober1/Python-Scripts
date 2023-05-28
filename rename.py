import os

# specify the path to your directory
dir_path = "/Users/dustinober/Downloads/DataQuest"

# iterate over all files in the directory
for filename in os.listdir(dir_path):
    # only process pdf files
    if filename.endswith(".pdf"):
        # remove the "Dustin-Ober--" part
        new_filename = filename.replace("Dustin-Ober--", "")
        # replace remaining "-" with " "
        new_filename = new_filename.replace("-", " ")

        # get full paths
        old_file_path = os.path.join(dir_path, filename)
        new_file_path = os.path.join(dir_path, new_filename)

        # rename the files
        os.rename(old_file_path, new_file_path)
