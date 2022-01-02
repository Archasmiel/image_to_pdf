from PIL import Image
import glob


def make_list_from_extensions(file_path: str, extensions: list):
    files = []
    for i in extensions:
        files.extend(glob.glob(rf'{file_path}\{i}'))
    return files


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
