def record_update(local_record):
    try:
        with open("gameLogic/record.txt", mode='w+', encoding='utf8') as file1:
            file1.write(str(local_record))
    except FileNotFoundError:
        print("Файл не найден. Укажите путь к файлу вручную.")
        exit()
    except PermissionError:
        print("Ошибка доступа к файлу.")
    except IOError:
        print("Ошибка записи в файл/ чтения файла.")
    # except OSError:
    #     print("Ошибка чтения из файла.")