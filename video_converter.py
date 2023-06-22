from ascii_converter import _convert_image
from time import sleep as sleep
from PIL import Image
from keyboard import is_pressed
import os
import sys
import cv2


class Video_manager:
    def __init__(self, selected_video, ascii_chars):
        self.selected_video = selected_video
        self.video_width = 50 
        self.video_height = 45
        self.ascii_chars = (
            r"$@B%8&WM#*oaj+~<>i!lI;:, " if ascii_chars is None else ascii_chars
        )

    def show_video_in_console(self):
        video_width = self.video_width
        video_height = self.video_height
        ascii_chars = self.selected_video
        os.system("cls")
        vidcap = cv2.VideoCapture(self.selected_video)
        stdout = os.fdopen(sys.stdout.fileno(), "wb", video_width * video_height)
        while True:
            success, image = vidcap.read()
            if not success or is_pressed('q'):
                break
            result = _convert_image(
                Image.fromarray(image), video_height, video_width, ascii_chars
            )
            os.system("cls")
            stdout.write(result.encode())
            sleep(0.016)