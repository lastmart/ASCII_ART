import sys
from PIL import Image
import argparse

def convert_image_to_ASCII_Art(image_path, path_to_save, heigth, width):
    image = Image.open(image_path)
    heigth = heigth if heigth is not None else image.height
    width = width if width is not None else image.width
    resized_image = image.resize((width, heigth))
    black_and_white_image = resized_image.convert("L")
    pixels = black_and_white_image.getdata() 
    ascii_chars = ['A', 'B', '.', ':', 'E', 'F', '@', 'H', '*', 'J', 'K', 'L',
                   'M', 'N', 'O', '|']
    changed_pixels = [ascii_chars[pixel // 17] for pixel in pixels]
    ascii_image = []
    for i in range(0, len(changed_pixels), width):
        ascii_image.append("".join(changed_pixels[i:i+width]))
    ascii_image = str("\n".join(ascii_image))
    with open(f"{path_to_save}/ascii_art.txt", 'w') as f:
        f.write(ascii_image) 

if sys.argv[1] in ['-h', '--help']:
    description = ["python3", 
                   "'path to main.py of this programm'", 
                   "'path to the image you want to convert'", 
                   "'path to the directory you want to save ASCII art'", 
                   "'width_of_picture_you_want'", 
                   "'height_of_picture_you_want'"] 
    description = ' '.join(description)
    parser = argparse.ArgumentParser(description = description)
    args = parser.parse_args()

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3 and len(args) != 5:
        raise SyntaxError("Number of arguments is not as expected")
    image_path = args[1]
    path_to_save = args[2]
    heigth = int(args[3]) if len(args) == 5 else None
    width = int(args[4]) if len(args) == 5 else None
    convert_image_to_ASCII_Art(image_path, path_to_save, heigth, width)