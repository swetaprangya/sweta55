import time
import os
import shutil
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:\Users\routd\OneDrive\Desktop"

#event handler class
class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"hey,{event.src_path}has been created!")
    def on_deleted(self,event):
        print(f"Oops! someone deleted {event.src_path}!")
    def on_modified(self,event):
        print(f"hay there!,{event.src_path} has been modified")
    def on_moved(self,event):
        print(f"someone moved{event.src_path}to{event.dest_path}")            

#Initialize Event Handler Class
event_handler=FileEventHandler()

#initialize Obsever
observer=Observer()

#schedule the observer
observer.schedule(event_handler,from_dir,Recursive=True)

#start the oserver
observer.start()
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stoped!")
    observer.stop()        
