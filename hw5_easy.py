# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil


def create_dir(path):
    try:
        os.mkdir(path)
        print('Успешно создано.')
    except FileExistsError:
        print('Невозможно создать папку. Нет такой папки.')


def delete_dir(path):
    try:
        os.removedirs(path)
        print('Успешно удалено.')
    except FileNotFoundError:
        print('Невозможно удалить папку. Нет такой папки.')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_folders():
    for file_or_folder in os.listdir():
        if os.path.isdir(file_or_folder):
            print(file_or_folder)


show_folders()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_file():
    file_name, ext = __file__.split('.')
    copy_file_name = file_name + '_copy.' + ext
    shutil.copy(__file__, copy_file_name)


if __name__ == '__main__':
    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        create_dir(dir_path)
        delete_dir(dir_path)
    show_folders()
    copy_file()

