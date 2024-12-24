from random import choice


def choose_word():
    try:
        file = open('gameLogic/wordslist.txt', encoding='utf8')  # Открытие файла с параметрами по умолчанию (для чтения)
    except FileNotFoundError:
        print("Файл не найден. Укажите путь к файлу вручную.")
        exit()
    except PermissionError:
        print("Ошибка доступа к файлу.")
    except IOError:
        print("Ошибка записи в файл/ чтения файла.")
    wordlist = file.readlines()
    wordlist = [line.rstrip().lower() for line in wordlist]
    word = choice(wordlist)
    progress = ['\u25A0'] * len(word)
    file.seek(0)
    file.close()
    return word, progress