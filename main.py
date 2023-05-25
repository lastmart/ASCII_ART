import argparse
from ascii_converter import convert_image_to_ASCII_Art
from ascii_gui import Gui


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


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    ui_parameters = [
        "Абсолютный путь до изображения",
        "Абсолютный путь, куда сохранить результат",
        "Высота ASCII art",
        "Ширина ASCII art",
        "Алфавит из символов",
    ]
    gui = Gui(ui_parameters, 3)
    gui.show_gui()
    convert_image_to_ASCII_Art(
        args.image_path, args.path_to_save, args.heigth, args.width, args.ascii_symbols
    )
