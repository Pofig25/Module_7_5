import os
import time

directory = "."                                                             # Указываем директорию для обхода

for root, dirs, files in os.walk(directory):                                # Используем os.walk для обхода директории
    for file in files:
        filepath = os.path.join(root, file)                                 # Формируем полный путь к файлу
        filetime = os.path.getmtime(filepath)                               # Получаем время последнего изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  # Форматируем время
        filesize = os.path.getsize(filepath)                                # Получаем размер файла в байтах
        parent_dir = os.path.dirname(filepath)                              # Получаем родительскую директорию файла

        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
            f'Родительская директория: {parent_dir}')                       # Выводим информацию о файле