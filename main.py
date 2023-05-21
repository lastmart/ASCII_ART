import sys
import argparse
from PIL import Image


help_description = [
    "python3",
    "'path to main.py of this programm'",
    "'path to the image you want to convert'",
    "'path to the directory you want to save ASCII art'",
    "'width_of_picture_you_want'",
    "'height_of_picture_you_want'",
]


def convert_image_to_ASCII_Art(image_path, path_to_save, heigth, width, ascii_chars):
    image = Image.open(image_path)
    new_heigth = heigth if heigth is not None else image.height
    new_width = width if width is not None else image.width
    resized_image = resize_image(image, new_width, new_heigth)
    pixels = [get_grayscaled_pixel(pixel) for pixel in resized_image.getdata()]
    changed_pixels = [
        ascii_chars[pixel // (255 // (len(ascii_chars) - 1))] for pixel in pixels
    ]
    ascii_image = []
    for i in range(0, len(changed_pixels), new_width):
        ascii_image.append("".join(changed_pixels[i : i + new_width]))
    ascii_image = str("\n".join(ascii_image))
    with open(f"{path_to_save}/ascii_art.txt", "w") as f:
        f.write(ascii_image)


def resize_image(image, new_width, new_height):
    scaled_image = Image.new(image.mode, (new_width, new_height), "white")
    width, height = image.size
    scale_x = new_width / width
    scale_y = new_height / height
    for y in range(new_height):
        for x in range(new_width):
            pixel = nearest_neighbour_interpolation(image, x, y, scale_x, scale_y)
            scaled_image.putpixel((x, y), pixel)
    return scaled_image


def nearest_neighbour_interpolation(image, x, y, scale_x, scale_y):
    x_nearest = int(round(x / scale_x))
    y_nearest = int(round(y / scale_y))
    return image.getpixel((x_nearest, y_nearest))


def get_grayscaled_pixel(pixel):
    red, green, blue = pixel[0:3]
    gray = int(0.2989 * red + 0.5870 * green + 0.1140 * blue)
    return gray


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Converts image to ISCII art")
    parser.add_argument(
        "-i", dest="image_path", type=str, help="Path to the converted image"
    )
    parser.add_argument(
        "-o", dest="path_to_save", type=str, help="Path to save ASCII art"
    )
    parser.add_argument(
        "--heigth",
        type=int,
        default=None,
        help="Heigth of ASCII art (defalt: height of image)",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=None,
        help="WIdth of ASCII art (defalt: width of image)",
    )
    parser.add_argument("ascii_symbols", type=str, help="Symbols to ASCII art")
    print(parser.parse_args())
    args = parser.parse_args()
    convert_image_to_ASCII_Art(
        args.image_path, args.path_to_save, args.heigth, args.width, args.ascii_symbols
    )