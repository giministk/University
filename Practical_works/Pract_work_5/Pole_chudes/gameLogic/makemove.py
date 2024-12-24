def make_move(progress, tries, word_hidden):
    ALPHABET = "абвгдеёжзиклмнопрстуфхцчшщъыьэюя"
    letter = input("Введите одну предполагаемую букву загаданного слова или все слово целиком: ")
    letter = letter.lower()
    if len(letter) == 1:
        try:
            ALPHABET.index(letter)
        except Exception:
            print("Недопустимый символ, используйте только буквы русского алфавита.")
            tries -= 1
            return(progress, tries)

        if letter in word_hidden and letter not in progress:

            print("Вы угадали букву!")
            progress[word_hidden.index(letter)] = letter
            tries -= 1
            return progress, tries

        elif word_hidden.count(letter) > 1 and progress.count(letter) < word_hidden.count(letter):

            print("Вы угадали букву!")
            progress[word_hidden.index(letter, ''.join(progress).rindex(letter)+1)] = letter

        else:

            print("Вы не угадали букву!")
            tries -= 1
            return (progress, tries)

    if letter == word_hidden:

        print("Вы угадали слово!")
        progress = word_hidden
        return (progress, tries)

    else:

        print("Вы ввели неверное слово")
        tries -= 1
        return (progress, tries)





