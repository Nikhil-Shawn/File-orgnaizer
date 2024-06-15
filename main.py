import os
import shutil

# Define the mapping of file extensions to directory names
EXTENSION_DIRS = {
    'pdf': 'PDFs',
    'docx': 'Word Documents',
    'doc': 'Word Documents',
    'rar': 'RAR Files',
    'zip': 'ZIP Files',
    'jpg': 'Images',
    'jpeg': 'Images',
    'png': 'Images',
    # Add more extensions and corresponding directories as needed
}

def organize_files(folder_path):
    # Create the target directories if they do not exist
    for dir_name in EXTENSION_DIRS.values():
        dir_path = os.path.join(folder_path, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Skip directories
        if os.path.isdir(os.path.join(folder_path, filename)):
            continue
        
        # Get the file extension
        file_extension = filename.split('.')[-1].lower()
        
        # Determine the target directory based on the file extension
        target_dir = EXTENSION_DIRS.get(file_extension)
        if target_dir:
            target_path = os.path.join(folder_path, target_dir, filename)
            source_path = os.path.join(folder_path, filename)
            shutil.move(source_path, target_path)
            print(f'Moved: {filename} to {target_dir}')

if __name__ == "__main__":
    # Input the folder path
    folder_path = input("Enter the path of the folder to organize: ")
    organize_files(folder_path)
    print("Files have been organized.")
