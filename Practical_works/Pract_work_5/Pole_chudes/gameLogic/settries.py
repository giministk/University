def set_tries(difficulty):
    difficulty = difficulty.lower()
    tries = 0
    if difficulty == "hard":
        tries = 3
    elif difficulty == "medium":
        tries = 5
    elif difficulty == "easy":
        tries = 7
    else:
        print("Введите правильное название уровня сложности.")
        exit()
    return tries