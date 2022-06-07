# Download-Folder-Python-Manager
 A script to monitor and manage your downloads folder and to place all newly downloaded files into sub folders to sort files by file types like documents, images, videos etc.

 This was created for my specific needs and will be updated to how I wish to structure my files. I have made it easy for anyone to change how they wish to structure their files, all you need to do is change your corressponding directories and add file extensions that you wish to sort into that file.

 ### Pip Installs required
 - shutil
 - watchdog
 - shortuuid

 ``` python -m pip install *pip library*```

 ### Change Source Directory
 This is the directory that will be observed for changes. When a file is add / created here it will then trigger watchdog to see if the file needs to be sorted.

 ```source_dest = "/Users/mrspe/Downloads/"```

 Change this to your downloads folder

 ### Change Destination Directories**
This is the directories where files will be sorted to. You can create as many as you wish with specific extensions that you require.

```
dest_dir_image = "/Users/mrspe/OneDrive - Waterford Institute of Technology/Desktop/Downloaded Images/"
dest_dir_video = "/Users\mrspe/OneDrive - Waterford Institute of Technology/Desktop/Downloaded Videos/"
dest_dir_3dprint = "/Users/mrspe/OneDrive - Waterford Institute of Technology/Desktop/Downloaded STLs/"
dest_dir_document = "/Users/mrspe/OneDrive - Waterford Institute of Technology/Desktop/Downloaded Documents/"
dest_dir_music = "/Users/mrspe/OneDrive - Waterford Institute of Technology/Desktop/Downloaded Music/"
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






