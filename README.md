Sure! Here's an updated version of the README to include both file and folder organizing features:

---

# File and Folder Organizer

This Python script organizes files and folders in a specified directory by sorting them into subfolders based on their file extensions and predefined categories. For example, all `.pdf` files will be moved to a "PDFs" folder, all `.jpg` files to an "Images" folder, and so on. Additionally, folders can be categorized based on specific keywords.

## Features

- Automatically organizes files by their extensions.
- Automatically organizes folders based on predefined categories.
- Supports a wide range of file types including documents, images, archives, and more.
- Easily customizable to support additional file types or modify existing behavior.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python 3 installed on your machine.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script with the following command:

    ```bash
    python file_organizer.py /path/to/your/folder
    ```

    Replace `/path/to/your/folder` with the path to the directory you want to organize.

### Example

```bash
python file_organizer.py C:/Users/YourUsername/Downloads
```

This will organize all files and folders in the `Downloads` folder into subfolders based on their types and predefined categories.

## Supported File Types

The script currently supports the following file types:

- **Documents**: `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.xls`, `.pptx`, `.ppt`
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`
- **Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
- **Media**: `.mp3`, `.mp4`, `.wav`, `.avi`, `.mkv`, `.mov`
- **Others**: Additional file types can be easily added by modifying the `file_type_folders` dictionary in the script.

## Supported Folder Categories

The script can organize folders into the following categories based on keywords in their names:

- **Games**: Keywords like `god of war`, `red dead`, `ark`, `subnautica`, `call of duty`, `cod`
- **Projects**: Keywords like `project`, `new site`, `web`, `node`, `react`, `hrm`, `human-resource`
- **Applications**: Keywords like `apps`, `applications`, `windows`, `nvidia`, `microsoft`, `toefl`
- **Miscellaneous**: Keywords like `misc`, `other`, `temp`

## Customization

To add support for additional file types or change the folder names:

1. Open the `file_organizer.py` script in a text editor.
2. Modify the `file_type_folders` dictionary to include new file extensions and their corresponding folder names.

    ```python
    file_type_folders = {
        'Documents': ['pdf', 'docx', 'doc', 'txt', 'xlsx', 'xls', 'pptx', 'ppt'],
        'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'svg'],
        'Archives': ['zip', 'rar', '7z', 'tar', 'gz'],
        'Media': ['mp3', 'mp4', 'wav', 'avi', 'mkv', 'mov'],
        # Add more categories and extensions as needed
    }
    ```

To add or modify folder categories:

1. Open the `file_organizer.py` script in a text editor.
2. Modify the `FOLDER_CATEGORIES` dictionary to include new keywords and their corresponding category names.

    ```python
    FOLDER_CATEGORIES = {
        'Games': ['games', 'god of war', 'red dead', 'ark', 'subnautica', 'call of duty', 'cod'],
        'Projects': ['project', 'new web', 'web', 'node', 'react', 'hrm', 'human-resource'],
        'Applications': ['apps', 'applications', 'windows', 'nvidia', 'microsoft', 'toefl'],
        'Miscellaneous': ['misc', 'other', 'temp']
        # Add more categories and keywords as needed
    }
    ```

## Contributing

Feel free to submit issues, fork the repository, and send pull requests with improvements or new features. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have any questions about the File Organizer, please [open an issue](https://github.com/Nikhil-Shawn/File-orgnaizer/issues) on GitHub.
