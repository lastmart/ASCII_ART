from ascii_converter import convert_image_to_ASCII_Art
from ascii_converter import save_ascii_image_in_file
from video_converter import Video_manager
from ascii_gui import Gui
import argparse


def call_image_converter(args):
    ascii_image = convert_image_to_ASCII_Art(
        args.image_path,
        args.height,
        args.width,
        args.ascii_symbols,
    )
    save_ascii_image_in_file(ascii_image, args.path_to_save)


def call_gui(args):
    gui_parameters = [
        "Абсолютный путь до изображения",
        "Абсолютный путь, куда сохранить результат",
        "Высота ASCII art",
        "Ширина ASCII art",
        "Алфавит из символов",
    ]
    gui = Gui(gui_parameters, initial_row=3)
    gui.show_gui()


def call_video_converter(args):
    video_manager = Video_manager(args.video_path, args.ascii_symbols)
    video_manager.show_video_in_console()


def create_parser():
    parser = argparse.ArgumentParser(description="Converts image or video to ASCII")
    subparsers = parser.add_subparsers(required=True, help="sub-command help")
    image_parser = subparsers.add_parser("image", help="Converts image to ASCII art")
    add_arguments_for_image_parser(image_parser)
    video_parser = subparsers.add_parser("video", help="Converts video to ASCII video")
    add_argument_for_video_parser(video_parser)
    gui_parser = subparsers.add_parser(
        "gui", help="Shows GUI for converting image to ASCII art"
    )
    gui_parser.set_defaults(func=call_gui)
    return parser


def add_argument_for_video_parser(parser):
    parser.add_argument(
        "-i", dest="video_path", type=str, help="Path to converted video"
    )
    parser.add_argument(
        "-a",
        dest="ascii_symbols",
        type=str,
        help="Symbols to ASCII art (default: $@B8&WM#*oaj+~<>i!lI;:, )"
    )
    parser.set_defaults(func=call_video_converter)


def add_arguments_for_image_parser(parser):
    parser.add_argument(
        "-i", dest="image_path", type=str, help="Path to the converted image"
    )
    parser.add_argument(
        "-o", dest="path_to_save", type=str, help="Path to save ASCII art"
    )
    parser.add_argument(
        "--height",
        type=int,
        default=None,
        help="Height of ASCII art (default: height of image)",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=None,
        help="Width of ASCII art (default: width of image)",
    )
    parser.add_argument(
        "-a", dest="ascii_symbols", type=str, help="Symbols to ASCII art"
    )
    parser.set_defaults(func=call_image_converter)


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    args.func(args)
