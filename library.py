from PIL import Image


def make_filename(num: int, extension: str):
    if num < 10:
        return f'00{num}.{extension}'
    elif num < 100:
        return f'0{num}.{extension}'
    else:
        return f'{num}.{extension}'


def load_image(file: str, pressure: float):
    image = Image.open(file).convert('RGB')
    width, height = image.size
    width, height = int(width*pressure), int(height*pressure)
    return image.resize((width, height))


def load_image_to_array(array: list, file: str, pressure: float):
    array.append(load_image(file, pressure))


def make_pdf_file(files: list, outputPath: str, pressure: float):
    first_page = load_image(files[0], pressure)
    images = []
    for num, val in enumerate(files):
        if num != 0:
            load_image_to_array(images, val, pressure)
    first_page.save(rf'{outputPath}\result.pdf', save_all=True, append_images=images)
