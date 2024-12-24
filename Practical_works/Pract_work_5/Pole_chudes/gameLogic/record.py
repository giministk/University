def record_update(local_record):
    try:
        with open("gameLogic/record_detected.txt", mode='r+', encoding='utf8') as file:
            r = int(file.readline())
            if local_record > r:
                r = local_record
                with open("gameLogic/record_detected.txt", mode='w', encoding='utf8') as file:
                    file.write(str(r))
    except FileNotFoundError:
        print("Файл не найден. Укажите путь к файлу вручную.")
        exit()
    except PermissionError:
        print("Ошибка доступа к файлу.")
    except IOError:
        print("Ошибка записи в файл/ чтения файла.")
    # except OSError:
    #     print("Ошибка чтения из файла.")