import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as st
from ascii_converter import convert_image_to_ASCII_Art
from ascii_converter import save_ascii_image_in_file


class Gui:
    def __init__(self, ui_parameters, initial_row):
        self.window = tk.Tk()
        self._image_helper = Image_helper(None, None, None)
        self.font_size = 15
        self.window.title("Конвертор изображения в ASCII art")
        self.window.geometry("500x300")
        frame = tk.Frame(self.window, padx=10, pady=10)
        frame.pack(expand=True)
        self._init_parameters(frame, initial_row, ui_parameters)
        self._init_buttons(frame, initial_row + len(ui_parameters))

    def _init_parameters(self, frame, initial_row, ui_parameters):
        position_arguments = []
        for i in range(initial_row, initial_row + len(ui_parameters)):
            parameter = ui_parameters[i - initial_row]
            parameter_lb = tk.Label(frame, text=parameter)
            parameter_lb.grid(row=i, column=1)
            parameter_tf = tk.Entry(frame)
            position_arguments.append(parameter_tf)
            parameter_tf.grid(row=i, column=2)
        self._image_helper.parameters = position_arguments

    def _init_buttons(self, frame, button_row):
        convert_button = tk.Button(
            frame,
            text="Конвертировать",
            command=lambda: self._call_converter(self._image_helper.parameters),
        )
        convert_button.grid(row=button_row, column=2)
        show_button = tk.Button(
            frame, text="Посмотреть результат", command=lambda: self._show_art()
        )
        show_button.grid(row=button_row, column=1)

    def show_gui(self):
        self.window.mainloop()

    def _call_converter(self, args):
        try:
            image_path = str(args[0].get())
            path_to_save = str(args[1].get())
            heigth = int(args[2].get())
            width = int(args[3].get())
            ascii_chars = str(args[4].get())
        except Exception:
            messagebox.showerror(
                "converter",
                "Введите все параметры прежде чем конвертировать изображение",
            )
            return None
        ascii_image = convert_image_to_ASCII_Art(image_path, heigth, width, ascii_chars)
        self._image_helper.ascii_art_file = save_ascii_image_in_file(
            ascii_image, path_to_save
        )
        self._image_helper.ascii_art = None
        messagebox.showinfo("converter", "Изображение успешно сконвертировано")

    def _show_art(self):
        with open(self._image_helper.ascii_art_file, "r") as f:
            ascii_art = "".join(f.readlines())

        self.art_window = tk.Tk()
        self.art_window.title("ASCII Art")

        text_area = st.ScrolledText(
            self.art_window,
            width=1000,
            height=600,
            font=("Courier New", self.font_size),
            wrap=None,
        )
        text_area.insert(tk.INSERT, ascii_art)
        text_area.configure(state="disabled")
        text_area.pack(fill="both", expand=True)
        self._image_helper.ascii_art = text_area

        self.art_window.bind("=", lambda e: self._change_font_size(text_area, 1))
        self.art_window.bind("+", lambda e: self._change_font_size(text_area, 1))
        self.art_window.bind("-", lambda e: self._change_font_size(text_area, -1))
        self.art_window.bind("_", lambda e: self._change_font_size(text_area, -1))
        self.art_window.mainloop(0)

    def _change_font_size(self, text_window, delta_size):
        if self.font_size + delta_size <= 0:
            return
        self.font_size += delta_size
        text_window.configure(font=("Courier New", self.font_size), wrap="none")


class Image_helper:
    def __init__(self, ascii_art_file, parameters, ascii_art):
        self.ascii_art_file = ascii_art_file
        self.parameters = parameters
        self.ascii_art = ascii_art
