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
        help="Width of ASCII art (defalt: width of image)",
    )
    parser.add_argument(
        "-a", dest="ascii_symbols", type=str, help="Symbols to ASCII art"
    )
    subparsers = parser.add_subparsers()
    create_gui(subparsers)
    return parser


def create_gui(subparsers):
    gui_parameters = [
        "Абсолютный путь до изображения",
        "Абсолютный путь, куда сохранить результат",
        "Высота ASCII art",
        "Ширина ASCII art",
        "Алфавит из символов",
    ]
    gui = Gui(gui_parameters, initial_row=3)
    parser_gui = subparsers.add_parser("gui", help="Shows GUI")
    parser_gui.set_defaults(func=gui.show_gui)


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    try:
        args.func()
    except AttributeError:
        convert_image_to_ASCII_Art(
            args.image_path,
            args.path_to_save,
            args.heigth,
            args.width,
            args.ascii_symbols,
        )
