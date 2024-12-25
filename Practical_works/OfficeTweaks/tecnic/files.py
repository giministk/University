import os


def return_curr_dir():
    return os.getcwd()


easter_flag_nofiles = 1


def find_files(*args, type: int = 0):
    global easter_flag_nofiles
    searching_for = tuple([*args])
    file_list = os.listdir(os.getcwd())
    file_nums = {}
    print(f'Поиск файлов с подстрокой {", ".join([*args])} в данном каталоге')
    if type == 0:
        for i in file_list:
            if i.endswith(searching_for):
                file_nums[len(file_nums) + 1] = i
                print(str(len(file_nums)) + ': ' + i)
    elif type == 1:
        for i in file_list:
            if i.startswith(searching_for):
                file_nums[len(file_nums) + 1] = i
                print(str(len(file_nums)) + ': ' + i)
    elif type == 2:
        for i in file_list:
            end = i.rindex('.')
            if i[:end].endswith(searching_for):
                file_nums[len(file_nums) + 1] = i
                print(str(len(file_nums)) + ': ' + i)
    elif type == 3:
        for i in file_list:
            end = i.rindex('.')
            for wanted in searching_for:
                if wanted in i[:end]:
                    file_nums[len(file_nums) + 1] = i
                    print(str(len(file_nums)) + ': ' + i)
    else:
        print("how did you get here?")
    if file_nums == {}:
        if easter_flag_nofiles:
            easter_flag_nofiles = 0
            print("\033[33m{}".format('\n' + ' ' * 10 + 'Advancement Made!\n'),
                  "\033[0m{}".format(' ' * 9 + 'We Need to Go Deeper\n'))
        print('Файлы не найдены. Попробуйте другой каталог')
        return file_nums
    return file_nums


def delete_files(choice, podstr):
    if choice == '1':
        for i in list(find_files(podstr, type=1).values()):
            try:
                os.remove(i)
                print(f'Файл {i} удален успешно')
            except PermissionError:
                print('Недостаточно прав для удаления!')
    elif choice == '2':
        for i in list(find_files(podstr, type=2).values()):
            try:
                os.remove(i)
                print(f'Файл {i} удален успешно')
            except PermissionError:
                print('Недостаточно прав для удаления!')
    elif choice == '3':
        for i in list(find_files(podstr, type=3).values()):
            try:
                os.remove(i)
                print(f'Файл {i} удален успешно')
            except PermissionError:
                print('Недостаточно прав для удаления!')

    else:
        if not podstr.startswith('.'):
            podstr = '.' + podstr
        for i in list(find_files(podstr, type=0).values()):
            try:
                os.remove(i)
                print(f'Файл {i} удален успешно')
            except PermissionError:
                print('Недостаточно прав для удаления!')