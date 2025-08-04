# File-organizer
📂 Python File Organizer
A simple Python script to automatically organize files (images, music, videos, documents, etc.) into folders based on their file types.

✅ Features
Organizes messy folders like Downloads, Desktop, etc.

Moves files into categorized folders: Images, Videos, Documents, Music, etc.
Works on Windows, macOS, and Linux
Lightweight, no external GUI or library (uses os and shutil)

os: Interacts with the operating system. Used for path operations, listing files, checking directories, etc.
shutil: Helps with file operations like copying and moving files.

🧠 How It Works
1.  Asks for the folder path ( Give path like: D:\Main\Child )
2.  Reads all files from the folder
3.  Identifies file type by extension (.jpg, .pdf, .mp3, etc.)
4.  Creates folders like Images/, Docs/, etc. if not exist
5.  Moves the files to their respective folders

NOTE: In last after complete this see you file system and it's organize in properway.
