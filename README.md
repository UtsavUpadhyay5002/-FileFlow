# 📂 Downloads Organizer 🚀

This Python project automatically organizes files in your Downloads folder. It moves files into appropriate subfolders based on their extensions. It checks for new files every 5 seconds and organizes them into folders like "Pictures", "Videos", "Documents", and more.

## ✨ Features

- 🖼️ Automatically moves image files (`.png`, `.jpeg`, `.jpg`) to the **Pictures** folder.
- 🎥 Moves video files (`.mp4`, `.mkv`, `.mp3`) to the **Videos** folder.
- 📄 Sorts text documents (`.txt`, `.pdf`, `.docx`, `.pptx`, `.csv`) into a "Downloaded_docs" folder with subfolders based on file type.
- 🖥️ Moves `.exe` files to an **executables** folder.
- 📦 Sorts `.zip` and `.drawio` files into their respective foldedrs.
- 💻 Organizes programming files (`.py`, `.java`, `.cpp`) into a "Downloaded_codes" folder.

## 📋 How It Works

1. The script monitors your **Downloads** folder for new files.
2. When a new file is detected, it is moved to an appropriate folder based on its file extension.
3. The script runs indefinitely, checking every 5 seconds for new files to organize.
4. Logs of files moved are stored in **"logs.txt"**

## 🛠️ Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/UtsavUpadhyay/FileFlow.git
    ```

2. Navigate to the project folder:
    ```bash
    cd FileFlow.git
    ```

3. Make sure you have Python installed (Python 3 recommended).

4. Create a logs.txt file in the project folder
    ```bash
    echo. > logs.txt
    ```

5. Run the Python script:
    ```bash
    py main.py
    ```

## 📦 Requirements

- Python 3
- No external libraries required at the moment.

## 🚀 Future Improvements

This is just the beginning! Future updates may include:
- 🔍 More advanced file sorting (e.g., by file size, creation date).
- 🖥️ A user interface for customizing folder structure.

## 🤝 Contributing

If you'd like to contribute, feel free to fork the repository, make changes, and submit a pull request. All contributions are welcome!

