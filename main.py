import sys
from PIL import Image
import numpy as np
import argparse


ascii_chars = [
        "A",
        "B",
        ".",
        ":",
        "E",
        "F",
        "@",
        "H",
        "*",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "|",
    ]

def convert_image_to_ASCII_Art(image_path, path_to_save, heigth, width):
    image = Image.open(image_path)
    new_heigth = heigth if heigth is not None else image.height
    new_width = width if width is not None else image.width
    resized_image = resize_image(image, new_width, new_heigth)
    black_and_white_image = resized_image.convert("L")
    pixels = black_and_white_image.getdata()
    changed_pixels = [ascii_chars[pixel // 17] for pixel in pixels]
    ascii_image = []
    for i in range(0, len(changed_pixels), new_width):
        ascii_image.append("".join(changed_pixels[i : i + new_width]))
    ascii_image = str("\n".join(ascii_image))
    with open(f"{path_to_save}/ascii_art.txt", "w") as f:
        f.write(ascii_image)

def resize_image(image, new_width, new_height):
    scaled_image = Image.new(image.mode, (new_width, new_height), 'white')
    width, height = image.size
    scale_x = new_width / width
    scale_y = new_height / height
    for y in range(new_height):
        for x in range(new_width):
            pixel = nearest_neighbour_interpolation(image, x, y, scale_x, scale_y)   
            scaled_image.putpixel((x, y),  pixel)
    return scaled_image

def nearest_neighbour_interpolation(image, x, y, scale_x, scale_y):
    x_nearest = int(np.round(x / scale_x))
    y_nearest = int(np.round(y / scale_y))
    return image.getpixel((x_nearest, y_nearest))

def get_grayscaled_pixel(pixel):
    red, green, blue = pixel[0:3]
    gray = int(0.2989 * red + 0.5870 * green + 0.1140 * blue)
    return gray, gray, gray

if sys.argv[1] in ["-h", "--help"]:
    description = [
        "python3",
        "'path to main.py of this programm'",
        "'path to the image you want to convert'",
        "'path to the directory you want to save ASCII art'",
        "'width_of_picture_you_want'",
        "'height_of_picture_you_want'",
    ]
    parser = argparse.ArgumentParser(description=" ".join(description))
    args = parser.parse_args()

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3 and len(args) != 5:
        raise SyntaxError("Number of arguments is not as expected")
    image_path = args[1]
    path_to_save = args[2]
    heigth = int(args[3]) if len(args) == 5 else None
    width = int(args[4]) if len(args) == 5 else None
    convert_image_to_ASCII_Art(image_path, path_to_save, heigth, width)