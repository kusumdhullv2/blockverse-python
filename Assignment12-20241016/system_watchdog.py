import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = r"C:\Users\31651\Downloads"        #path should be set to the directory you want to watch for changes.
log_file = r"C:\kusum-python\log\log.txt"    #path where logs are saved whenever a file event occurs.

# Saving all loging information in log.txt
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%Y %H:%M:%S')

"""filename=log_file: Specifies the file where log messages are saved.
level=logging.INFO: Sets the logging level to INFO, meaning it will record informational messages, such as file events.
format and datefmt: Defines how log messages and timestamps are formatted in the log file. """

# Custom event handler
class FileHandler(FileSystemEventHandler):

    def rename_if_exists(self, path):
        if os.path.exists(path):
            base, extension = os.path.splitext(path)
            counter = 1
            new_path = f"{base}({counter}){extension}"
            # Increment counter until unique file name is found
            while os.path.exists(new_path):
                counter += 1
                new_path = f"{base}({counter}){extension}"
            return new_path
        return path

    def on_created(self, event):
        if not event.is_directory:                       #checks that the event checks a file and not a directory.
            logging.info(f"File created: {event.src_path}")
            print(f"File created: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            logging.info(f"File deleted: {event.src_path}")
            print(f"File deleted: {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory:
            logging.info(f"File modified: {event.src_path}")
            print(f"File modified: {event.src_path}")

# Initialize and start observer
event_handler = FileHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)     #Every 2 seconds, it prints "Monitoring directory..." to show program is active
        print("Monitoring directory...") 
except KeyboardInterrupt:                   #The program stops when you press Ctrl+C or ctrl+delete
    print("Monitoring stopped.")
    observer.stop()

observer.join()  #Waits for the observer thread to complete
