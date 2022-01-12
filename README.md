<details><summary>[ENG] ENGLISH GUIDE</summary>
<p>

# ImgToPdf
This project contains program, which is able to convert images to pdf files(with choosable extensions).<br />

## Usage
#### *Downloading*
Clone or download repository to your machine.<br />
Just keep in mind fact, that all you need for program to run is **main.py** and **library.py** files in exact same folder.

#### *Configuring*
```python
input_path = rf'C:\PngToPdf'
extensions = [
    '*.png',
    '*.jpg',
    '*.jpeg',
]

file_pressure = 1
output_path = rf'C:\PngToPdf'
```
- **extensions** - list of extensions that program will check in input path
- **input_path** - path with all your files with determined extensions
> **Warning!**<br /> Folder with your files must NOT contain corrupted/damaged files.<br /> Also extensions must be correct(no .py, .java, .pptx and other non-image).
- **file_pressure** - recommended to type 0..1, in that way you gain compressed images file with lower size 
- **output_path** - path where program will save "result.pdf" file

#### *Output*
On program output you'll get result.pdf file with all your images from input directory.

# Software
Project made in **PyCharm 2021.3** with compiler set as **Python 3.7**.

</p>
</details>

<details><summary>[RUS] РУССКИЙ ГАЙД</summary>
<p>
  
# ImgToPdf
Этот проет был задуман для автоматического преобразования изображений в файл pdf.
  
## Использование
#### *Загрузка и запуск*
Чтобы получить проект, склонируйте его себе на машину или скачайте его в виде архива.<br />
Всё что вам нужно для запуска это **main.py** и **library.py** в той же самой папке.

#### *Настройка*
```python
input_path = rf'C:\PngToPdf'
extensions = [
    '*.png',
    '*.jpg',
    '*.jpeg',
]

file_pressure = 1
output_path = rf'C:\PngToPdf'
```
- **extensions** - список расширений для файлов, которые будут преобразованы;
- **input_path** - путь в папку с файлами, где располагаются все нужные файлы для преобразования;
> **Warning!**<br /> В папке не должны быть поломанные файлы.<br /> Также необходимы правильные расширения файлов с изображениями.
- **file_pressure** - настройка сжатия изображений;
> Рекомендуется ставить от 0 до 1, иначе будет то же самое качество но с большим размером. 
- **output_path** - путь для исходного файла pdf.

#### *Выход*
На выходе программы получаем файл **result.txt** в папке **output_path** с преобразованными изображениями.

# ПО
Проект сделан в **PyCharm 2021.3** с компилятором **Python 3.7**.
  
</p>
</details>
