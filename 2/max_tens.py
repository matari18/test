def max_tens(twos: int, threes: int, fours: int) -> int:
    """
    На вход подаются 3 числа: кол-во двоек, кол-во троек, кол-во четверок.
    На выходе выдает максимальное количество  десяток, которые можно из них составить.
    Составляются наборы вида:
    (2, 4, 4)
    (3, 3, 4)
    (3, 3, 2, 2)
    :param twos: количество двоек.
    :param threes: количество троек.
    :param fours: количество четверок.
    :return: количество составленных десяток.
    """

    tens = 0

    # (2, 4, 4)
    while twos >= 1 and fours >= 2:
        tens += 1
        twos -= 1
        fours -= 2

    # (3, 3, 4)
    while threes >= 2 and fours >= 1:
        tens += 1
        threes -= 2
        fours -= 1

    # (3, 3, 2, 2)
    while twos >= 2 and threes >= 2:
        tens += 1
        twos -= 2
        threes -= 2

    return tens


# Проверка
print(max_tens(1, 2, 3))  #2
print(max_tens(0, 0, 4))  #0
print(max_tens(100, 100, 3))  #51
print(max_tens(100, 200, 300))  #200
