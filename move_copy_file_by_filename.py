import os
import shutil

root_dir = 'path/to/root/directory'
new_folder = 'path/to/new/folder'

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.startswith('01') or filename.startswith('02'):
            old_file_path = os.path.join(dirpath, filename)
            new_file_path = os.path.join(new_folder, filename)
            shutil.copy2(old_file_path, new_file_path)
