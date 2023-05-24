import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as st
from ascii_convertor import convert_image_to_ASCII_Art


class Gui:
    def __init__(self, ui_parameters, initial_row):
        self.window = tk.Tk()
        self._image_helper = Image_helper(None, None, None)
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
            command=lambda: self._call_convertor(self._image_helper.parameters),
        )
        convert_button.grid(row=button_row, column=2)
        show_button = tk.Button(
            frame, text="Посмотреть результат", command=lambda: self._show_art()
        )
        show_button.grid(row=button_row, column=1)

    def show_gui(self):
        self.window.mainloop()

    def _call_convertor(self, args):
        try:
            image_path = str(args[0].get())
            path_to_save = str(args[1].get())
            heigth = int(args[2].get())
            width = int(args[3].get())
            ascii_chars = str(args[4].get())
        except Exception:
            messagebox.showerror(
                "convertor",
                "Введите все параметры прежде чем конвертировать изображение",
            )
            return None
        self._image_helper.ascii_art_file = convert_image_to_ASCII_Art(
            image_path, path_to_save, heigth, width, ascii_chars
        )
        self._image_helper.ascii_art = None
        messagebox.showinfo("convertor", "Изображение успешно сконвертировано")

    def _show_art(self):
        with open(self._image_helper.ascii_art_file) as f:
            ascii_art = "".join(f.readlines())

        self.art_window = tk.Tk()
        self.art_window.title("ASCII Art")
        text_area = st.ScrolledText(
            self.art_window, width=140, height=40, font=("Courier New", 15)
        )
        text_area.grid(column=0, pady=10, padx=10)
        text_area.insert(tk.INSERT, ascii_art)
        text_area.configure(state="disabled")
        self._image_helper.ascii_art = text_area
        self._init_scale_art_buttons()
        self.art_window.mainloop(0)

    def _init_scale_art_buttons(self, button_row):
        frame = tk.Frame(self.art_window, padx=10, pady=10)
        frame.pack(expand=True)
        convert_button = tk.Button(
            frame,
            text="+",
            command=lambda: self._scale_image(1),
        )
        convert_button.grid(row=button_row, column=1)
        show_button = tk.Button(
            frame,
            text="-",
            command=lambda: self._scale_image(-1)
        )
        show_button.grid(row=button_row, column=1)

    def _scale_image(self, inc):
        pass

class Image_helper:
    def __init__(self, ascii_art_file, parameters, ascii_art):
        self.ascii_art_file = ascii_art_file
        self.parameters = parameters
        self.ascii_art = ascii_art
