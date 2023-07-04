from PIL import Image


def convert_image_to_ASCII_Art(image, heigth: int, width: int, ascii_chars):
    if isinstance(image, str):
        try:
            image = Image.open(image)
        except FileNotFoundError as e:
            raise e from ValueError("You specified the wrong path to the image") 
    else:
        try:
            image = Image.fromarray(image)
        except Exception:
            raise TypeError("The image has the wrong format")
    new_heigth = heigth if heigth is not None else image.height
    new_width = width if width is not None else image.width
    if ascii_chars is None:
        raise ValueError("Ascii chars isn't selected")
    return _convert_image(image, new_heigth, new_width, ascii_chars)


def _convert_image(image, heigth, width, ascii_chars):
    resized_image = resize_image(image, width, heigth)
    pixels = [get_grayscaled_pixel(pixel) for pixel in resized_image.getdata()]
    char_segments_count = 255 / len(ascii_chars)
    changed_pixels = [
        3 * ascii_chars[int(pixel / char_segments_count)] for pixel in pixels
    ]
    ascii_image = []
    for i in range(0, len(changed_pixels), width):
        ascii_image.append("".join(changed_pixels[i : i + width]))
    ascii_image = str("\n".join(ascii_image))
    return ascii_image


def save_ascii_image_in_file(ascii_image, path_to_save):
    file_name = f"{path_to_save}/ascii_art.txt"
    try:
        with open(file_name, "w") as f:
            f.write(ascii_image)
    except FileNotFoundError as e:
        raise e from ValueError("You specified the wrong path to save the image") 
    return file_name


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