from ascii_converter import convert_image_to_ASCII_Art
from time import sleep
from keyboard import is_pressed
import os
import sys
import cv2


class Video_manager:
    video_width = 50
    video_height = 45

    def __init__(self, selected_video, ascii_chars):
        if selected_video[-4:] != ".mp4":
            raise ValueError("You should select an .mp4 file")
        self.selected_video = selected_video
        self.ascii_chars = (
            r"$@B8&WM#*oaj+~<>i!lI;:, " if ascii_chars is None else ascii_chars
        )

    def show_video_in_console(self):
        os.system("cls")
        vidcap = cv2.VideoCapture(self.selected_video)
        stdout = os.fdopen(
            sys.stdout.fileno(), "wb", self.video_width * self.video_height
        )
        while True:
            success, image = vidcap.read()
            if not success or is_pressed("q"):
                break
            result = convert_image_to_ASCII_Art(
                image, self.video_height, self.video_width, self.ascii_chars
            )
            os.system("cls")
            stdout.write(result.encode())
            stdout.flush()
            sleep(0.016)