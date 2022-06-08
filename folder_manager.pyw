import os
import time
import shutil
import shortuuid
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from configparser import ConfigParser

realpath_dir = os.path.dirname(os.path.realpath(__file__))
file = realpath_dir + "\config.ini" #Read in config file directories
config = ConfigParser()
config.read(file)

dest_dir_image = config['destination']['images']
dest_dir_video = config['destination']['videos']
dest_dir_3dprint = config['destination']['3dprints']
dest_dir_document = config['destination']['documents']
dest_dir_music = config['destination']['music']

image_extension = ('.jpg', '.png', '.gif', '.webp', '.tiff', '.tif', '.psd', '.raw', '.bmp', '.heif', '.indd', 'jpeg', '.jpe', '.jif', '.jfif', '.jfi', '.jp2', '.svg', '.svgz', '.ai', '.eps')
video_extensions = ('.mp4', '.mov', '.wmv', '.avi', '.avichd', '.flv', '.flv4', '.swf', '.mkv', '.webm')
print3d_extensions = ('.stl', '.obj', '.gcode', '.vrml', '.3mf', '.x3g', '.amf')
document_extension = ('.pdf', '.doc', 'docx', '.txt', '.odt', '.xls', '.xlsx', '.ods', '.ppt', '.pptx')
music_extension = ('.mp3', '.acc', '.ogg', '.flac', 'alac', '.wav', '.aiff', '.dsd', '.pcm')

def move(src, dest, name):
    file_exists = os.path.exists(dest + name) #Make sure the file name doesnt already exist in destination folder
    if not file_exists:
        shutil.move(src + name, dest + name)
    else:
        new_name = shortuuid.uuid() + name #Create random UUID to add infront of the name then move the file
        os.rename(src + name, src + new_name)
        shutil.move(src + new_name, dest + new_name)

def match_file(source_dest):
    with os.scandir(source_dest) as entries:
        for entry in entries:
            if entry.is_file:
                filename = entry.name
                if filename.endswith(image_extension): #Check for Image
                    move(source_dest, dest_dir_image,entry.name)
                elif filename.endswith(video_extensions): #Check for Videos
                    move(source_dest, dest_dir_video,entry.name)
                elif filename.endswith(document_extension): #Check for Documents
                    move(source_dest, dest_dir_document,entry.name)
                elif filename.endswith(music_extension): #Check for Music
                    move(source_dest, dest_dir_music,entry.name)
                elif filename.endswith(print3d_extensions): #Check for 3DPrint Files
                    move(source_dest, dest_dir_3dprint,entry.name)


class OnMyWatch:

    source_dest = config['source']['src']

    def __init__(self):
        self.observer = Observer()
    
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.source_dest, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            #print("Observer Stopped")

        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        
        elif event.event_type == 'created' or event.event_type == 'modified':
            match_file(OnMyWatch.source_dest)

if __name__ == "__main__":
    watch = OnMyWatch()
    watch.run()
