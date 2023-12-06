# Download Folder Sorting Automation

import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

folder_to_track = r"C:\Users\User\Downloads"
folder_destination = folder_to_track


file_types = {'.pdf': 'PDFs', '.xlsx': 'Excel', 
              '.docx': 'Word', '.pptx': 'PowerPoint', 
              '.jpg': 'Images', '.png': 'Images', 
              '.gif': 'Images', '.mp3': 'Audio', 
              '.mp4': 'Video', '.zip': 'Compressed',
              '.rar': 'Compressed', '.7z': 'Compressed',
              '.exe': 'Executables', '.py': 'Code',
              '.ipynb': 'Code', '.csv': 'Data'}

for types in file_types:
    folder = os.path.join(folder_destination, file_types[types])
    if not os.path.exists(folder):
        os.makedirs(folder)

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            name, extension = os.path.splitext(filename)
            extension = extension.lower()
            if extension in file_types:
                file_destination = os.path.join(folder_destination, file_types[extension])
                file_source = os.path.join(folder_to_track, filename)
                shutil.move(file_source, file_destination)

event_handler = MyHandler()
Observer = Observer()

Observer.schedule(event_handler, folder_to_track, recursive=True)
Observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    Observer.stop()

Observer.join()
