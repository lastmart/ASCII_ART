# ASCII_ART
### __What this program can do?__
It's a task solution from [anytask](https://anytask.org/course/1030). 
This program can convert image into file that will contain the symbolic interpretation of that image
or show video in console. 
### __How does it work?__
There are two ways to interact: via command line or GUI.
#### Command line:
If you need to convert an _image to ASCII art_, you need to write: `python3 main.py image`    
and then specify these parameters:

| Parameter        | Description                                    |
|------------------|------------------------------------------------|
| -i IMAGE_PATH    | Path to the converted image                    |
| -o PATH_TO_SAVE  | Path to save ASCII art                         |
| --height HEIGHT  | Height of ASCII art (default: height of image) |
| --width WIDTH    | Width of ASCII art (default: width of image)   |
| -a ASCII_SYMBOLS | Symbols to ASCII art                           |
 
    Example: python3 main.py image -i "C:\Users\egore\OneDrive\Изображения\ryan-gosling-blade-runner-2049.jpg" --height 120 --width 120 -o  "C:\Users\egore\OneDrive\Документы" -a "AB.:EF@H*JKLMNO|" 

If you need to convert a _video to ASCII video_, you need to write: `python3 main.py video`    
and then specify these parameters:

| Parameter        | Description                                              |
|------------------|----------------------------------------------------------|
| -i VIDEO_PATH    | Path to converted video                                  |
| -a ASCII_SYMBOLS | Symbols to ASCII art (default: $@B8&WM#*oaj+~<>i!lI;:, ) |

    Example: python main.py video -i "C:\Users\egore\OneDrive\Рабочий стол\sample.mp4" -a "AB.:EF@H*JKLMNO| "

### GUI:
You can call the command: `python3 main.py gui`  
You can increase/decrease the size of the image in view mode on the interface using `+` and `-` on the keyboard
