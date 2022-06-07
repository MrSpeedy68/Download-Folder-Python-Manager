import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

source_dest = "/Users/mrspe/Downloads"
dest_dir_image = "/Users/mrspe/OneDrive - Waterford Institute of Technology/Desktop/Downloaded Images"
dest_dir_video = "/Users\mrspe/OneDrive - Waterford Institute of Technology/Desktop/Downloaded Videos"
dest_dir_3dprint = "/Users/mrspe/OneDrive - Waterford Institute of Technology/Desktop/Downloaded STLs"
dest_dir_document = "/Users/mrspe/OneDrive - Waterford Institute of Technology/Desktop/Downloaded Documents"
dest_dir_music = "/Users/mrspe/OneDrive - Waterford Institute of Technology/Desktop/Downloaded Music"

with os.scandir(source_dest) as entries:
    for entry in entries:
        if entry.is_file:
            if ".pdf" in entry.name: 
                print(entry.name)

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S')
#     path = source_dest
#     event_handler = LoggingEventHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)
#     observer.start()
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()
