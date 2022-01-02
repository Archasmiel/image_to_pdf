from library import *


# path to your files (this example for one exact folder)
input_path = rf'C:\PngToPdf'
extensions = [
    '*.png',
    '*.jpg',
    '*.jpeg',
]

# pressure of images - type pressure as coefficient
# it must be between 0 and 1 for pressured files
# more than 1 will give you no sufficient result of quality
# comparing to 1 - bigger size, same quality
file_pressure = 1
output_path = rf'C:\PngToPdf'

# images path array
images = make_list_from_extensions(input_path, extensions)

print(f'\nAll files, compiled into pdf with compress coefficient {file_pressure}:')
for num, val in enumerate(images):
    print(f'[{num+1}]: {val}')

make_pdf_file(images, output_path, file_pressure)
print(f'\nResult was compiled to {output_path}\\result.pdf.')
