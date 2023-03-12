def generate_crossword(data):
    words = data["__words__"]
    words.sort(key=len)

    first_letters = {}

    def create_list_let(word):
        return [letter for letter in word]

    if len(words) <= 5:
        n = round(max([len(word) for word in words]) * 1.5)
    elif len(words) <= 10:
        n = round(max([len(word) for word in words]) * 2)
    else:
        n = round(max([len(word) for word in words]) * 2.5)
    word = words[-1]
    matrix = []
    for i in range(n):
        matrix.append(['_' for i in range(n)])
    for i in range(len(word)):
        matrix[n // 2][(n - len(word)) // 2 + i] = create_list_let(word)[i]

    i = 0
    j = 0
    letter = False
    flag = True
    capacity = True
    counter = 0
    while capacity == True:
        while i < n:  # Проход по столбцам матрицы
            while j <= n:  # Проход по столбцам матрицы
                if matrix[i][j] != "_":  # Нашли букву
                    for k in range(len(word)):  # Проверяем есть ли совпадающие буквы
                        if create_list_let(word)[k] == matrix[i][
                            j]:  # Нашли совпадающую букву в выбранном слове и в матрице
                            # Смотрим чтобы слово при вставлении не вылезло за поле
                            if (j - 1 - k >= 0 and i - 1 >= 0 and i + 1 < n and j + len(word) - k < n and j - k >= 0):
                                if (matrix[i][j - 1 - k] == "_" and matrix[i - 1][j - 1 - k] == "_" and matrix[i + 1][
                                    j - 1 - k] == "_"):  # Проверяем чтобы перед сдовом не было других слов, решил не писать в одну строку
                                    if (matrix[i][j + len(word) - k] == "_" and matrix[i - 1][j + len(word) - k] == "_" and
                                            matrix[i + 1][
                                                j + len(word) - k] == "_"):  # Исправить возможные баги если слово около границы поля
                                        letter = True
                                        j -= k  # Ставим "курсор" на место первой буквы вписываемого слова
                                        first = j  # Смотрим, будет ли слово вставляться через клетку от других слов
                                        last = j + len(word)
                                        while (first <= last):
                                            if matrix[i][
                                                first] == "_":  # Потенциальные баги если вставляем слово на границе поля
                                                if matrix[i - 1][first] != "_" or matrix[i + 1][first] != "_":
                                                    flag = False
                                            first += 1
                                        for x in range(
                                                len(word)):  # Смотрим можно ли вписать слово с учётом уже стоящих букв
                                            if matrix[i][j + x] != "_" and create_list_let(word)[x] != matrix[i][
                                                j + x]:  # Ищем "Конфликты букв"
                                                flag = False
                                    if letter == True:
                                        break
                            else:
                                flag = False  # Сюда слово не вписываем и идём дальше, запилить такое же для вертикали
                                # Если True значит конфликтов нет и можно вписать слово
                    if flag == True and letter == True:
                        for l in range(len(word)):  # Вписываем слово
                            if l == 0:
                                counter += 1
                                first_letters[word] = [j, i, counter]
                            matrix[i][j] = create_list_let(word)[l]
                            j += 1
                        for v in range(n):
                            print(*matrix[v])
                        if len(words) == 0:
                            capacity = False
                            break
                        words.pop(-1)  # Удаляем нахуй вписанное слово, ты сука мои нервы уже потрепало
                        if len(words) == 0:
                            capacity = False
                            break
                        word = words[-1]
                        flag = True
                        letter = False
                    else:
                        j += len(word)
                        if (j > n):
                            i += 1
                            j = 0
                        flag = True
                        letter = False  # Ставим курсор после слова
                else:
                    j += 1
                if j == n:
                    j = 0
                    i += 1
                if i == n:
                    # Не смогли вставить слово по горизонтали
                    i = 0
                    j = 0
                    break
            break
        # Если по горизонтали не получилось вставить, то пробуем вставить по вертикали
        print("Пробуем вставить во вертикали")
        i = 0
        j = 0
        # Вставляем слова по вертикали
        while j < n:  # Проход по столбцам матрицы
            while i <= n:  # Проход по столбцам матрицы
                if matrix[i][j] != "_":  # Нашли букву
                    for k in range(len(word)):  # Проверяем есть ли совпадающие буквы
                        if create_list_let(word)[k] == matrix[i][
                            j]:  # Нашли совпадающую букву в выбранном слове и в матрице
                            # Смотрим чтобы слово при вставлении не вылезло за поле
                            if (i - 1 >= 0 and j - 1 >= 0 and j + 1 < n and i + len(word) - k < n and i - k >= 0):
                                if (matrix[i - 1 - k][j] == "_" and matrix[i - 1 - k][j - 1] == "_" and matrix[i - 1 - k][
                                    j + 1] == "_"):  # Проверяем чтобы перед сдовом не было других слов, решил не писать в одну строку
                                    if (matrix[i + len(word) - k][j] == "_" and matrix[i + len(word) - k][j - 1] == "_" and
                                            matrix[i + len(word) - k][
                                                j + 1] == "_"):  # Исправить возможные баги если слово около границы поля
                                        letter = True
                                        i -= k  # Ставим "курсор" на место первой буквы вписываемого слова
                                        first = i  # Смотрим, будет ли слово вставляться через клетку от других слов
                                        last = i + len(word)
                                        while (first <= last):
                                            if matrix[first][
                                                j] == "_":  # Потенциальные баги если вставляем слово на границе поля
                                                if matrix[first][j - 1] != "_" or matrix[first][j + 1] != "_":
                                                    flag = False
                                            first += 1
                                        for x in range(
                                                len(word)):  # Смотрим можно ли вписать слово с учётом уже стоящих букв
                                            if matrix[i + x][j] != "_" and create_list_let(word)[x] != matrix[i + x][
                                                j]:  # Ищем "Конфликты букв"
                                                flag = False
                                    if letter == True:
                                        break
                            else:
                                flag = False  # Сюда слово не вписываем и идём дальше, запилить такое же для вертикали

                                # Если True значит конфликтов нет и можно вписать слово
                    if flag == True and letter == True:
                        for l in range(len(word)):
                            if l == 0:
                                counter += 1
                                first_letters[word] = [j, i, counter]
                            # Вписываем слово
                            matrix[i][j] = create_list_let(word)[l]
                            i += 1
                        for v in range(n):
                            print(*matrix[v])
                        if len(words) == 0:
                            capacity = False
                            break
                        words.pop(-1)  # Удаляем нахуй вписанное слово, ты сука мои нервы уже потрепало
                        if len(words) == 0:
                            capacity = False
                            break
                        word = words[-1]
                        flag = True
                        letter = False
                    else:
                        i += len(word)
                        if (i > n):
                            j += 1
                            i = 0
                        flag = True
                        letter = False
                        # Ставим курсор после слова
                else:
                    i += 1
                if i == n:
                    i = 0
                    j += 1
                if j == n:
                    if len(words) == 0:
                        capacity = False
                        break
                    words.pop(-1)
                    for i in range(n):
                        print(*matrix[i])
                    if len(words) == 0:
                        capacity = False
                        break
                    word = words[-1]
                    i = 0
                    j = 0
                    break
            break
    res_data = {"matrix": matrix, "first_letters": first_letters}
    return res_data
