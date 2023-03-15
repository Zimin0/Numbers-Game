""" 
ИИПИ - исходя из правил игры.
В общем, принцип не очень математически красивый, но рабочий. Поле мы представляем как матрицу (main_matrix). 
Требуется реализовать механику, чтобы игра определяла, когда стоит добавлять...
...новые чиселки. Для реализации данной механии и будем использовать принцип разбиения матрицы поля на 2 списка. 
Один (A) будет просто прочтением матрицы по строкам (приложение 1), а второй по столбцам (приложение 2).
Алгоритм, который проверяет, нужно ли добавлять еще чиселки(ходов больше нет) реализован в функции is_valid. В ней присутствуют 2 функции -

gorizontal_check - проходит по списку A, проверяя:

    a) Если элементы стоят рядом и на одной строке - доступный ход есть.
    б) Если элементы стоят рядом и на одной строке и между ними есть 1 или больше нулей (отсутствие элемента на деле) - доступный ход есть.
    в) Если элементы стоят рядом, но на разных строках - между ними должно быть хотя бы 2 нуля (ИИПИ) - тогда ход возможен. 
Вводится счетчик zero_count - который хранит количество нулей между парой чисел.
Имеются два "указателя" - right и left. Они идут друг за другом, указывая на соседние последовательные элементы. Но как только right встретит ноль - left останавливается на...
...последнем ненулевом элементе, который был до заветного нуля. Right шурует разведывать дальше и идет до тех пор, пока не встретит ненулевой элемент, считая встетившиеся нули на своем пути.


2я функция в is_valid - 
vertikav_check gorizontal_check - проходит уже по транспонированному списку A - тобишь A_T. Алгоритм тот же, что и в gorizontal_check, с отличием только в том, что...
...идем мы, получается, по столбцам. Правила проверки идентичные.


"""

""" -----Приложение 1-2 -----
main_matrix = [
    [1,2,3,4,5,6,7,8,9],
    [1,1,1,2,1,3,1,4,1],
    [5,1,6,1,7,1,8,1,9]
    ]

Тогда A = [1,2,3,4,5,6,7,8,9,1,1,1,2,1,3,1,4,1,5,1,6,1,7,1,8,1,9]
А_T уже будет = [1,1,5,2,1,1,3,1,6,4,2,1,5,1,7,6,3,1...]
A_T - "T" потому что A_T - транспонированная матрица матрицы A - вышмат епрст аххаах. 
"""




def cout_matrix(matrix):
    """ Красивый вывод матрицы."""
    tmp = []
    tmp = sum(matrix, []) # раскрытие списка - из [[1,2],[4,1]] в [1,2,4,1]
    k = 0
    print(" ------------------")
    print('|', end='')
    for i in tmp:
        if k % 9 == 0 and k != 0:
            print('|', end=' ')
            print()
            print('|', end='')
        if i == 0:
            print('-', end=' ')
            k += 1
            continue
        print(i, end=' ')
        k += 1
    print('|', end=' ')
    print("\n ------------------")
    print()
    print()

def add_numers():
    """ Добавляет чиселки, когда ходов уже нет."""
    global main_matrix # оправдано
    A = sum(main_matrix, [])
    k = 0
    tmp = []
    for num in A:
        if k % 9 == 0 and k != 0:
            if tmp != []:
                main_matrix.append(tmp)
            tmp = []
        if num == 0:
            continue
        tmp.append(num)
        k += 1
    if len(tmp) < 10:
        for _ in range(9-len(tmp)):
            tmp.append(0)
    main_matrix.append(tmp)
    
def gorizontal_check(A, user_input):
    "Строка за строкой проходимся по массиву. Проверяем валидность введенного пользователем хода."
    is_valid = False # Правильно ли введенное пользователем значение 
    user_input = sorted(user_input)  # сортируем ввод, т к это нужно для цикла - он пойдет от меньшего до большего
    x1 = user_input[0][0] - 1 # минус один - потому что в массивах нумерация с нуля
    y1 = user_input[0][1] - 1
    x2 = user_input[1][0] - 1
    y2 = user_input[1][1] - 1

    line = x1
    zero_count = 0
    # был ли перескок со строки на строку - находятся ли введенные пользователем числа на разных строках
    if abs(x1 - x2) != 0:
        pereskok = True
    else:
        pereskok = False

    proshel = False # флаг того, что цикл уже зашел за второй искомый элемент.
    col = y1
    # начальная проверка на условие парности или равности 10ти
    # Числа одинаковые или в сумме дают 10------------------------------# На введенных координатах не стоят нули-# Не введена одно и тоже число ( все координаты не равны)
    if ((A[x1][y1] == A[x2][y2]) or (A[x1][y1] + A[x2][y2] == 10)) and (A[x1][y1] != 0 and A[x2][y2] != 0) and (x1 != x2 or y1 != y2):
        while line < len(A) and not(proshel):
            while col < 9: # - 9 длина одной строки - фиксированная, поэтому использую константу "9"
                if A[line][col] == 0: # 0 - уже зачеркнутое число 
                    zero_count += 1 # счетчик нулей между, которые мы нашли для данной пары.
                if line == x2 and col == y2: # дошли до второго числа
                    if pereskok and zero_count >= 0: # если числе на разных строках - тогда между ними должно быть минимум два пустых места (нуля)
                        return True
                    if not(pereskok) and zero_count >= 0:  #Если элементы стоят рядом и на одной строке и между ними есть 1 или больше нулей 
                        return True
                else:
                    if A[line][col] != 0 and (line != x1 or col != y1): 
                        # если на пути перебора встречается число, не равное нулю или введенным пользователем числам   
                        return False
                col += 1  
            line += 1
            col = 0
    return is_valid

def vertikav_check(A_T, user_input,A):
    is_valid = False # Правильно ли введенное пользователем значение 

    # Нужно отсортировать значения по столбцу
    user_input = sorted(user_input)
    if user_input[0][1] > user_input[1][1]:
        user_input.reverse()
    
    x1 = user_input[0][0] - 1 # - 1 потому что в массивах нумерация с нуля
    y1 = user_input[0][1] - 1
    x2 = user_input[1][0] - 1
    y2 = user_input[1][1] - 1


    line = y1
    zero_count = 0
    # был ли перескок со строки на строку - находятся ли введенные пользователем числа на разных строках
    if abs(y1 - y2) != 0:
        pereskok = True
    else:
        pereskok = False
    
    proshel = False # флаг того, что цикл уже зашел за второй искомый элемент.
    # начальная проверка на условие парности или равности 10ти
    col = x1
    # Числа одинаковые или в сумме дают 10---------------------------------# На введенных координатах не стоят нули----# Не введена одно и тоже число
    if ((A_T[y1][x1] == A_T[y2][x2]) or (A_T[y1][x1] + A_T[y2][x2] == 10)) and (A_T[y1][x1] != 0 and A_T[y2][x2] != 0) and (x1 != x2 or y1 != y2):
        while line < 9 and not(proshel):
            while col < len(A):
                if A_T[line][col] == 0: # 0 - уже зачеркнутое число
                    zero_count += 1
                if line == y2 and col == x2: # дошли до второго числа
                    if pereskok and zero_count >= 2:
                        return True
                    if not(pereskok) and zero_count >= 0:
                        return True
                else:
                    if A_T[line][col] != 0 and (line != y1 or col != x1): 
                        # если на пути перебора встречается число, не равное нулю или введенным пользователем числам   
                        return False
                col += 1
            line += 1
            col = 0
    return is_valid

def rewrite_A(main_matrix):
    """ Перезаполняет список A, когда главная матрица main_matrix изменяется."""
    A = []
    for i in range(len(main_matrix)):
        tmp = []
        for j in range(9):
            tmp.append(main_matrix[i][j])
        A.append(tmp)
    return A

def rewrite_AT(main_matrix):
    """ Перезаполняет список A_T, когда главная матрица main_matrix изменяется."""
    A_T = []
    for i in range(9):
        tmp = []
        for j in range(len(main_matrix)):
            tmp.append(main_matrix[j][i])
        A_T.append(tmp)
    return A_T

def is_valid(turn, A, A_T, main_matrix):

    tmp = sum(turn, []) # раскрытие списка - из [[1,2],[4,1]] в [1,2,4,1]
    if tmp[0] > len(main_matrix) or tmp[2] > len(main_matrix) : # проверка на то, что индекс строки не превышает кол-ва строк.
        return False
    for num in tmp: # проверка, что координаты от 1 до 9
        if num > 9 or num < 1:
            return False

    t1 = gorizontal_check(A, turn)
    t2 = vertikav_check(A_T, turn, A)
    return (t1 or t2)

def get_users_coordinated():
    """Получение ввода от пользователя. """
    inp = None
    inp = input("Координаты:")
    print()
    if inp == "exit": 
        return False, [[0,0], [0,0]]
    if inp == "add":
        return "add", [[0,0], [0,0]]
    


    inp = list(map(int, inp.split()))
    input1 = [[0,0],[0,0]]
    input1[0][0] = inp[0]
    input1[0][1] = inp[1]
    input1[1][0] = inp[2]
    input1[1][1] = inp[3]
    input1 = sorted(input1) # для вертикального нужно сортировать по второму значению
    return True, input1

def insert_zeros(main_matrix, turn):
    """ Вставляет нули на места, на которые указал юзер."""
    for coords in turn:
        x = coords[0]-1
        y = coords[1]-1
        main_matrix[x][y] = 0
    return main_matrix

def possible_to_make_next_turn(A, A_T):
    """Проверка, стоит ли добавлять еще числа - возможен ли еще один ход."""

    def is_pair_or_10(a,b):
        """Проверка на условие валидности хода из задачи."""
        return (a == b) or (a + b == 10)

    # Проверка Горизонтально расположенных чисел, с помощью которых можно сделать ход.
    is_valid = False
    A_temp = sum(A, []) # раскрытие списка - из [[1,2],[4,1]] в [1,2,4,1]
    left = 0
    right = 1
    zero_count = 0
    need_amout_zero = 1
    #print("Possible horizontal turns:")
    while right < len(A_temp):
        if A_temp[right] == 0: # если в массиве встречается ноль
            zero_count = 0 # текущеее кол-во встреченных нулей
            while right < len(A_temp): # пока не дойдем до элемента, который != нулю.
                if A_temp[right] != 0:
                    break 
                if (right) % 9 == 0: # каждый 9й элемент - это перескок на другую строку, здесь мы его и отлавливаем
                    need_amout_zero = 2 # при перескоке со строки на строку между элементами должно быть не менее 2 нулей между, чтобы сделать ход.
                zero_count += 1
                right += 1 # сморим следующий правый элемент, при том не двигая левый. 
            
            if right < len(A_temp):
                if (zero_count >= need_amout_zero) and is_pair_or_10(A_temp[left], A_temp[right]) and ((right) % 9 != 0): # 1 условие - если количество нулей, которые мы нашли в данный момент между двумя числами >= требуемому
                    #print(f"v1={A_temp[left]}, v2={A_temp[right]}")
                    is_valid = True
                
            left = right # перепрыгиваем через нули левым элементом
            right += 1
            need_amout_zero = 1 # минимальное кол-во нулей, которое должно стоять между числами на одной строке, чтобы можно было сделать ход
            continue # мы уже просмотрели число, стоящее через несколько нулей, значит можно переходить к след иттерации

        if is_pair_or_10(A_temp[left], A_temp[right]):
            if (right) % 9 != 0:
                is_valid =  True
        right += 1
        left += 1
    
    # Проверка вертикально расположенных чисел, с помощью которых можно сделать ход.
    # Все то же самое, что и в прошлой проверке. Только теперь смотрим на числа, расположенные вертикально.
    A_temp = sum(A_T, []) # раскрытие списка - из [[1,2],[4,1]] в [1,2,4,1]
    left = 0
    right = 1
    zero_count = 0
    need_amout_zero = 1
    #print("Possible vertical turns:")
    while right < len(A_temp):
        if A_temp[right] == 0: 
            zero_count = 0 
            while right < len(A_temp): 
                if A_temp[right] != 0:
                    break 
                if (right) % len(A_T) == 0: # каждый n-й элемент - это перескок на другую строку, здесь мы его и отлавливаем
                    need_amout_zero = 2 
                zero_count += 1
                right += 1 
            if right < len(A_temp):   
                if (zero_count >= need_amout_zero) and is_pair_or_10(A_temp[left], A_temp[right]) and ((right) % 3 != 0): # 1 условие - если количество нулей, которые мы нашли в данный момент между двумя числами >= требуемому
                    is_valid =  True
            left = right 
            right += 1
            need_amout_zero = 1 
            continue 

        if is_pair_or_10(A_temp[left], A_temp[right]):
            if (right) % 3 != 0: 
                is_valid = True
        right += 1
        left += 1
    return is_valid



    
def main():
    
    main_matrix = [
        [1,2,3,4,5,6,7,8,9],
        [1,1,1,2,1,3,1,4,1],
        [5,1,6,1,7,1,8,1,9]
        ]

    A = []
    A_T = []
    A = rewrite_A(main_matrix)
    A_T = rewrite_AT(main_matrix)

    print("\n------------------------------WELCOME!------------------------------")
    print("Вводите координаты в формате [x1 y1 x2 y2], например: 1 2 1 5")
    print("Для выхода из игры введите \"exit\"")
    print("--------------------------------------------------------------------\n")


    cout_matrix(main_matrix)
    while True: # бесконечный цикл 
        # Проверка на ввод одного и того же элемента

        if not(possible_to_make_next_turn(A, A_T)): # если валидных ходов нет - добавляет чиселки
            add_numers()
            A = rewrite_A(main_matrix) 
            A_T = rewrite_AT(main_matrix)
            cout_matrix(main_matrix)
        value = get_users_coordinated() # получаем ввод от юзера
        if value[0] == 'add':
            add_numers()
            A = rewrite_A(main_matrix)
            A_T = rewrite_AT(main_matrix)
            cout_matrix(main_matrix)
            continue
        if not(value[0]):  # для работы ввода exit 
            break
        user_coords = value[1] # координаты юзера

        if is_valid(user_coords, A, A_T, main_matrix): # если ход валиден 
            main_matrix = insert_zeros(main_matrix, user_coords) # убираем введенные пользователем числа - вставляем вместо них нули
            A = rewrite_A(main_matrix)
            A_T = rewrite_AT(main_matrix)
        else:
            print('---------------')
            print("Невозможный ход!")
            print('---------------\n')
        cout_matrix(main_matrix)

    #x = (2 + 4*(n-1) - n) % 27 + (n-1) // 9 # А эту формулу я выводил 1 час, обидно, что не пригодилась :( 

main()      