import os 
from tkinter.filedialog import askdirectory

path = askdirectory(title="Select a Folder to Organize")
list_files = os.listdir(path)

locals = {
   'Images': ['.png', '.jpeg', '.jpg'],
    'Excel': ['.xlsx'],
    'PDF': ['.pdf'],
    'CSV': ['.csv'],
    'Photoshop': ['.psd'],
    'CorelDRAW': ['.cdr'],
    'XML': ['.xml'],
    'SQL Script': ['.sql'],
    'Text and Word Documents': ['.txt', '.docx', '.doc'],
    'Executable': ['.exe'],
    'Compressed Archives': ['.zip', '.rar'],
    'Video (MP4)': ['.mp4'],
    'Video (MOV)': ['.mov']
}

for file in list_files:
  name, extension = os.path.splitext(f"{path}/{file}")
  for folder in locals:
    if extension in locals[folder]:
      if not os.path.exists(f"{path}/{folder}"):
        os.mkdir(f"{path}/{folder}")
      os.rename(f"{path}/{file}", f"{path}/{folder}/{file}")