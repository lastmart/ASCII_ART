import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as st
from ascii_converter import convert_image_to_ASCII_Art
from ascii_converter import save_ascii_image_in_file


class Gui:
    font_size = 15

    def __init__(self, ui_parameters, initial_row):
        self.art_window = None
        self.window = tk.Tk()
        self.window.title("Конвертор изображения в ASCII art")
        self.window.geometry("500x300")
        frame = tk.Frame(self.window, padx=10, pady=10)
        frame.pack(expand=True)
        self._init_ui_parameters(frame, initial_row, ui_parameters)
        self._init_buttons(frame, initial_row + len(ui_parameters))

    def _init_ui_parameters(self, frame, initial_row, ui_parameters):
        ui_entries = []
        for i in range(initial_row, initial_row + len(ui_parameters)):
            parameter = ui_parameters[i - initial_row]
            parameter_lb = tk.Label(frame, text=parameter)
            parameter_lb.grid(row=i, column=1)
            parameter_tf = tk.Entry(frame)
            ui_entries.append(parameter_tf)
            parameter_tf.grid(row=i, column=2)
        self._ui_entries = ui_entries

    def _init_buttons(self, frame, button_row):
        convert_button = tk.Button(
            frame,
            text="Конвертировать",
            command=self._call_converter,
        )
        convert_button.grid(row=button_row, column=2)
        show_button = tk.Button(
            frame, text="Посмотреть результат", command=self.show_art
        )
        show_button.grid(row=button_row, column=1)

    def show_gui(self):
        self.window.mainloop()

    def _call_converter(self):
        (
            image_path,
            path_to_save,
            height,
            width,
            ascii_chars,
        ) = self._unpack_parameters_from_ui_entries()
        ascii_image = convert_image_to_ASCII_Art(image_path, height, width, ascii_chars)
        self.ascii_art_file = save_ascii_image_in_file(ascii_image, path_to_save)
        messagebox.showinfo("converter", "Изображение успешно сконвертировано")

    def _unpack_parameters_from_ui_entries(self):
        entries = self._ui_entries
        image_path = entries[0].get()
        path_to_save = entries[1].get()
        height = entries[2].get()
        width = entries[3].get()
        ascii_chars = entries[4].get()
        if not (
            len(image_path)
            and len(path_to_save)
            and len(height)
            and len(width)
            and len(ascii_chars)
        ):
            messagebox.showerror(
                "converter",
                "Введите все параметры прежде чем конвертировать изображение",
            )
            raise ValueError
        try:
            width = int(width)
            height = int(height)
        except ValueError:
            messagebox.showerror(
                "converter",
                "Высота и ширина имеют числовые значения",
            )
            raise ValueError
        return image_path, path_to_save, height, width, ascii_chars

    def show_art(self):
        try:
            with open(self.ascii_art_file, "r") as f:
                ascii_art = "".join(f.readlines())
        except AttributeError:
            messagebox.showerror(
                "converter",
                "Прежде чем увидеть изображение нужно сначала сконвертировать его",
            )
            return
        try:
            self.art_window.destroy()
        except (AttributeError, tk.TclError):
            pass
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
