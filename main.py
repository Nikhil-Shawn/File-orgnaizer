import os
import shutil

# Organize files into categories
file_type_folders = {
    'PDFs': ['pdf'],
    'Word Documents': ['docx', 'doc'],
    'RAR Files': ['rar'],
    'ZIP Files': ['zip'],
    'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'svg'],
    'Text Files': ['txt'],
    'Excel Files': ['xlsx', 'xls'],
    'PowerPoint Files': ['pptx', 'ppt'],
    'Archives': ['7z', 'tar', 'gz'],
    'Media': ['mp3', 'mp4', 'wav', 'avi', 'mkv', 'mov'],
    'Install Files': ['exe', 'msi', 'jar']
}

def organize_files(folder_path):
    # Create the target directories if they do not exist
    for dir_name in file_type_folders.keys():
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
        target_dir = None
        for dir_name, extensions in file_type_folders.items():
            if file_extension in extensions:
                target_dir = dir_name
                break
        
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
