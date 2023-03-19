import os
import shutil
import sys

from myfunctions import purchase_list, selection_block, attention_msg, separator
import birthdayforever


def menu_func():
    while True:
        print('1. Create new folder')
        print('2. Delete folder')
        print('3. Copy folder')
        print('4. Show current folder')
        print('5. Show folders only')
        print('6. Show files only')
        print('7. SYS info')
        print('8. Show author')
        print('9. Play game')
        print('10. Account')
        print('11. Change directory')
        print('12. Exit')

        separator('-', 20)
        choice_item = input('Select menu item: ')

        if choice_item == '1':
            m_1_create_new_file()
        elif choice_item == '2':
            m_2_delete_folder()
        elif choice_item == '3':
            m_3_copy_folder()
        elif choice_item == '4':
            m_4_show_cur_folder()
        elif choice_item == '5':
            m_5_show_fold_only()
        elif choice_item == '6':
            m_6_show_files_only()
        elif choice_item == '7':
            m_7_sys_info()
        elif choice_item == '8':
            m_8_show_author()
        elif choice_item == '9':
            birthdayforever.play_game()
        elif choice_item == '10':
            attention_msg('Не реализовано')
        elif choice_item == '11':
            m_11_change_dir()
        elif choice_item == '12':
            break
        else:
            attention_msg('Unknown item!')


def m_1_create_new_file():
    folder_name = input('Input new folder name: ')
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    else:
        attention_msg('папка уже существует')


def m_2_delete_folder():
    del_folder_name = input('Input folder name for delete: ')
    if os.path.exists(del_folder_name):
        os.rmdir(del_folder_name)
    else:
        attention_msg('папка отсутствует')


def m_3_copy_folder():
    copy_folder_name = input('Input folder name for copy: ')
    copied_folder_name = input('Input new name for copied folder: ')
    shutil.copytree(copy_folder_name, copied_folder_name)


def m_4_show_cur_folder():
    selection_block(sys.path)


def m_5_show_fold_only():
    print("Folders in work directory:")
    for item in os.listdir():
        if os.path.isdir(item):
            selection_block(item)


def m_6_show_files_only():
    for item in os.listdir():
        selection_block(item)


def m_7_sys_info():
    print('System information: ')
    print(f'User name: {os.getlogin()}')
    print(f'System platform: {os.name}')


def m_8_show_author():
    selection_block(f'Author is {os.getlogin()}')


def m_11_change_dir():
    new_directory = input("Введите новую директорию: ")
    if os.path.exists(new_directory):
        os.chdir(new_directory)
        print(f"Рабочая директория изменена на {new_directory}.")
    else:
        print(f"Директория {new_directory} не существует.")
