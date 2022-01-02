from library import *


# path to your files (this example for one exact folder)
file_path = rf'C:\PngToPdf'

# pressure of images - type pressure as coefficient
# it must be between 0 and 1 for pressured files
# more than 1 will give you no sufficient result of quality
# comparing to 1 - bigger size, same quality
file_pressure = 0.66

# images path array
all_images = [
    rf'{file_path}\{make_filename(1, "jpg")}',
    rf'{file_path}\{make_filename(2, "jpg")}',
]

make_pdf_file(all_images, file_path, file_pressure)
