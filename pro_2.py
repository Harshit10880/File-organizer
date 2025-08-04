import os
import shutil

# os: Interacts with the operating system. Used for path operations, listing files, checking directories, etc.
# shutil: Helps with file operations like copying and moving files.

# Define categories and associated extensions
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css'],
    'Others': []  # for unknown types
}

# Set your folder path here (e.g., Downloads or Desktop)
folder_path = input("\nEnter folder path to organize: ")

# Function to get category by file extension
def get_category(extension):
    for category, extensions in file_types.items():
        if extension.lower() in extensions:
            return category
    return 'Others'

# Organize files
def organize_files():
    if not os.path.exists(folder_path):
        print("❌ Folder path does not exist!")
        return

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file_name)
        category = get_category(ext)

        target_dir = os.path.join(folder_path, category)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # Move the file
        shutil.move(file_path, os.path.join(target_dir, file_name))
        print(f"✅ Moved: {file_name} → {category}/")

    print("\n🎉 All files organized successfully!")

# Run the function
organize_files()
