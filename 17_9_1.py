def binary_search(array, element, left, right):
    if left > right:
        return (right, left)

    middle = (right + left) // 2
    if array[middle] == element:
        return (middle-1, middle)
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)

def answer(list_of,ans):
    x, y = ans
    if x == -1:
        print('Ответ: числа, меньше введенного, нет, второй индекс -', y)
    elif y == len(list_of):
        print('Ответ: первый индекс -', x, ', числа, больше введенного, нет')
    else:
        print('Ответ(индексы):', x, y)

def begin_program(string, number):
    print('Number = ', number)
    print('List = ', string)
    list_of_strings = string.split()
    list_of_numbers = list(map(int, list_of_strings))
    qsort(list_of_numbers, 0, len(list_of_numbers) - 1)
    print('Sort list = ', list_of_numbers)
    print('Index:', [*range(len(list_of_numbers))])
    res = binary_search(list_of_numbers, number, 0, len(list_of_numbers) - 1)
    answer(list_of_numbers, res)
    print('-------------------------------')

string = input("Введите числа через пробел:")
number = int(input('Введите число:'))
begin_program(string, number)


# #tests
# number = 6
# string = '1 7 8 3 4 5'
# begin_2(string,number)

# number = 0
# string = '1 7 8 3 4 5'
# begin_2(string,number)

# number = 10
# string = '1 7 8 3 4 5'
# begin_2(string,number)

# number = 5
# string = '1 7 8 3 4 5'
# begin_2(string,number)

# number = 1
# string = '1 7 8 3 4 5'
# begin_2(string,number)