# Download-Folder-Python-Manager
A script to monitor and manage your downloads folder and to place all newly downloaded files into sub folders to sort files by file types like documents, images, videos etc.

This was created for my specific needs and will be updated to how I wish to structure my files. I have made it easy for anyone to change how they wish to structure their files, all you need to do is change your corressponding directories and add file extensions that you wish to sort into that file.

### Pip Installs required
- shutil
- watchdog
- shortuuid

``` python -m pip install *pip library*```
 
# Run The File
This script is meant to run in the background with no GUI and run at startup. Here are the steps to run the file in the background at startup for both Windows and Linux.

To simply run the file,
```python folder_manager.pyw```

## Windows Setup
To let make the file run at startup and in the background, I have provided a batch file .bat which needs to be placed inside of Windows startup shell. To do this follow these steps,

```Ctrl + R```

Enter "*shell:startup*" inside and hit enter.

Copy the **foldermanager.bat** file inside of this directory. The batch file will need adjusting as the directories will be different for everyone and where your computer holds the pythonw.exe and where you hold the script.

The batch file,
```
start C:\msys64\mingw64\bin\python3w.exe "C:\Users\mrspe\Desktop\Local Github\Download-Folder-Python-Manager\folder_manager.pyw"
```

Change the first directory to the location of your pythonw.exe as we want python to run the file with no GUI, by default using the command "python" should recognize the .pyw file but it didn't in my case. The second directory is the location where you hold the folder_manager.py script.

That's it on startup the file should run in the background and manage your downloads folder.

## Linux Setup
TO DO

### Change Directories
This is the directory that will be observed for changes. When a file is added / created here it will then trigger watchdog to see if the file needs to be sorted.
Inside of *config.ini* there are various options to change **Source** and **Destination** directories.

```
[source]
src = \Users\mrspe\Downloads\
```

Change **src** to your downloads folder

Inside of **destination** there are 5 options for file types to sort, I will add more in the future but I created these to my needs.
This is the directories where files will be sorted to. You can create as many as you wish with specific extensions that you require.

```
[destination]
images = \Users\mrspe\Desktop\Downloaded Images\
videos = \Users\mrspe\Desktop\Downloaded Videos\
3dprints = \Users\mrspe\Desktop\Downloaded STLs\
documents = \Users\mrspe\Desktop\Downloaded Documents\
music = \Users\mrspe\Desktop\Downloaded Music\
```

## Adding or changing directories and extension to filter
To add aditional extensions and folders to filter simply adjust the **match_file** method.

```
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
```

Simply add additional else if statements to this with the endswith argument being your extensions tuple.

```
document_extension = ('.pdf', '.doc', 'docx', '.txt', '.odt', '.xls', '.xlsx', '.ods', '.ppt', '.pptx')
```

The **move** method requires the source directory and the destination directory and the file name.

Thats it! enjoy the python script and if there is additional functionality that would be interesting or would make this script better dont hesitate to let me know!.






