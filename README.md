# ASCII_ART
### __What this program can do?__
It's a task solution from [anytask](https://anytask.org/course/1030).
This program can convert image into file that will contain the symbolic interpretation of that image.
### __How does it works?__
There are two ways to interact: via command line or GUI.
#### Command line:
You must enter the following parameters:
| parameter        |  description                                 |
|------------------|----------------------------------------------|
| -h, --help       |  show this help message and exit             |
| -i IMAGE_PATH    | Path to the converted image                  |
| -o PATH_TO_SAVE  | Path to save ASCII art                       |
| --heigth HEIGTH  | Heigth of ASCII art (defalt: height of image)|
| --width WIDTH    | Width of ASCII art (defalt: width of image)  |
| -a ASCII_SYMBOLS | Symbols to ASCII art                         |

You first specify the parameter name listed in the left column, and then the value itself.
Example: `python3` main.py -i "C:\Users\egore\OneDrive\Изображения\ryan-gosling-blade-runner-2049.jpg" --heigth 120 --width 120 -o  "C:\Users\egore\OneDrive\Документы" -a "AB.:EF@H*JKLMNO|"
### GUI:
You can call the command:
`python3` main.py gui
