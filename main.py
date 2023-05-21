import argparse
import tkinter as tk
from tkinter import messagebox
from PIL import Image


def convert_image_to_ASCII_Art(image_path, path_to_save, heigth, width, ascii_chars):
    image = Image.open(image_path)
    new_heigth = heigth if heigth is not None else image.height
    new_width = width if width is not None else image.width
    resized_image = resize_image(image, new_width, new_heigth)
    pixels = [get_grayscaled_pixel(pixel) for pixel in resized_image.getdata()]
    char_segments_count = 255 // (len(ascii_chars) - 1)
    changed_pixels = [ascii_chars[pixel // char_segments_count] for pixel in pixels]
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


def create_parser():
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
    return parser


ui_parameters = [
    "Абсолютный путь до изображения",
    "Абсолютный путь, куда сохранить результат",
    "Высота ASCII art",
    "Ширина ASCII art",
    "Алфавит из символов",
]


def get_tkinter_input():
    window = tk.Tk()
    window.title("Конвертор изображения в ASCII art")
    window.geometry("500x300")
    frame = tk.Frame(window, padx=10, pady=10)
    frame.pack(expand=True)
    inital_row = 3
    position_aruments = []
    for i in range(inital_row, inital_row + len(ui_parameters)):
        parameter = ui_parameters[i - inital_row]
        parameter_lb = tk.Label(frame, text=parameter)
        parameter_lb.grid(row=i, column=1)
        parameter_tf = tk.Entry(frame)
        position_aruments.append(parameter_tf)
        parameter_tf.grid(row=i, column=2)

    cal_btn = tk.Button(
        frame,
        text="Конвертировать",
        command=lambda: convertor_helper(position_aruments),
    )
    cal_btn.grid(row=inital_row + len(ui_parameters), column=2)

    window.mainloop()


def convertor_helper(args):
    try:
        image_path = str(args[0].get())
        path_to_save = str(args[1].get())
        heigth = int(args[2].get())
        width = int(args[3].get())
        ascii_chars = str(args[4].get())
    except Exception:
        messagebox.showerror(
            "convertor", "Введите все параметры прежде чем конвертировать изображение"
        )
        return None

    convert_image_to_ASCII_Art(image_path, path_to_save, heigth, width, ascii_chars)
    messagebox.showinfo("convertor", "Изображение успешно сконвертировано")


if __name__ == "__main__":
    parser = create_parser()
    get_tkinter_input()
    args = parser.parse_args()
    convert_image_to_ASCII_Art(
        args.image_path, args.path_to_save, args.heigth, args.width, args.ascii_symbols
    )
