import os
from myfunctions import purchase_list

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

        purchase_list(input('Select menu: '))

        if choice == '1':
            m_1_create_new_file()
        elif choice == '2':
            m_2_delete_folder()
        elif choice == '12':
            break


def m_1_create_new_file():
    folder_name = input('Input new folder name: ')
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    else:
        print('папка существует')


def m_2_delete_folder():
    del_folder_name = input('Input folder name for delete: ')
    if os.path.exists(del_folder_name):
        os.rmdir(del_folder_name)
    else:
        print('папка отсутствует')

