File Organizer Script
This Python script helps you organize files in a specified folder by moving them into subfolders based on their file extensions. It categorizes files into folders such as “Images,” “Excel,” “PDF,” and more.

Usage
Run the script.
A dialog will prompt you to select the folder you want to organize.
The script will then create subfolders for each file type (based on the extensions) and move the files accordingly.
Supported File Types
Images: .png, .jpeg, .jpg
Excel: .xlsx
PDF: .pdf
CSV: .csv
Photoshop: .psd
CorelDRAW: .cdr
XML: .xml
SQL Script: .sql
Text and Word Documents: .txt, .docx, .doc
Executable: .exe
Compressed Archives: .zip, .rar
Video (MP4): .mp4
Video (MOV): .mov
Example
Suppose you have a folder with the following files:

my_folder/
    file1.jpg
    file2.xlsx
    file3.pdf
    ...

After running the script, the folder structure will be:

my_folder/
    Images/
        file1.jpg
    Excel/
        file2.xlsx
    PDF/
        file3.pdf
    ...
