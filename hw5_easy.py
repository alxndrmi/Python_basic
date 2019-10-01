# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil


def create_dirs():
    try:
        for i in range(1, 10):
            dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
            os.mkdir(dir_path)
    except FileExistsError:
        print('Folders already exist')

def delete_dirs():
    try:
        for i in range(1, 10):
            dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
            os.removedirs(dir_path)
    except FileNotFoundError:
        print('No such folders')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_folders():
    for file_or_folder in os.listdir(os.getcwd()):
        file_or_folder_path = os.path.join(os.getcwd(), file_or_folder)
        if os.path.isdir(file_or_folder_path):
            print(file_or_folder)


show_folders()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_file():
    file_name, ext = __file__.split('.')
    copy_file_name = file_name + '_copy.' + ext
    shutil.copy(__file__, copy_file_name)


if __name__ == '__mail__':
    create_dirs()
    delete_dirs()
    show_folders()
    copy_file()

