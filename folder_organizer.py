import os
import shutil

# Dictionary to map folder names to their corresponding categories
FOLDER_CATEGORIES = {
    'Games': ['games','god of war', 'red dead', 'ark', 'subnautica', 'call of duty', 'cod'],
    'Projects': ['project', 'new site', 'web', 'node', 'react', 'hrm', 'human-resource'],
    'Applications': ['apps', 'applications', 'windows', 'nvidia', 'microsoft', 'toefl'],
    'Miscellaneous': ['misc', 'other', 'temp']
}

# Directories to skip from being categorized into specific categories
DIRECTORIES_TO_SKIP = ['Games', 'Projects', 'Applications', 'Git', 'Miscellaneous']

# Function to check if a directory should be skipped
def should_skip_directory(dir_name):
    # Example: skip directories starting with system prefixes or in system directories
    system_prefixes = ['$AV_', '$VAULT']
    system_directories = ['C:\\Windows', 'C:\\Program Files', 'C:\\Program Files (x86)']
    
    if any(dir_name.startswith(prefix) for prefix in system_prefixes):
        return True
    
    if any(dir_name.lower().startswith(dir_path.lower()) for dir_path in system_directories):
        return True
    
    if dir_name.lower() in map(str.lower, DIRECTORIES_TO_SKIP):
        return True
    
    return False

def organize_folders(folder_path):
    # Create target directories if they do not exist
    for category in FOLDER_CATEGORIES.keys():
        dir_path = os.path.join(folder_path, category)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # Loop through all subdirectories in the folder
    for dir_name in os.listdir(folder_path):
        dir_path = os.path.join(folder_path, dir_name)
        
        # Skip if it's not a directory or if it should be skipped
        if not os.path.isdir(dir_path) or should_skip_directory(dir_name):
            continue
        
        # Check if the directory matches any of the defined categories
        matched_category = None
        for category, keywords in FOLDER_CATEGORIES.items():
            if any(keyword in dir_name.lower() for keyword in keywords):
                matched_category = category
                break
        
        if matched_category:
            # Determine target directory path
            target_dir_path = os.path.join(folder_path, matched_category)
        else:
            # If no category matches, move to Miscellaneous
            matched_category = 'Miscellaneous'
            target_dir_path = os.path.join(folder_path, matched_category)
        
        target_path = os.path.join(target_dir_path, dir_name)
        
        # Check if the target path already exists
        if os.path.exists(target_path):
            print(f'Skipped moving: {dir_name} to {matched_category} (destination path already exists)')
        else:
            # Move the directory to its corresponding category folder
            shutil.move(dir_path, target_path)
            print(f'Moved: {dir_name} to {matched_category}')

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to organize: ")
    organize_folders(folder_path)
    print("Folders have been organized.")
