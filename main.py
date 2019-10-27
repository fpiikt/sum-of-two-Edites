"""
  Автор: Морозов Алексей, группа P42552
  Ссылка на сайт-портфолио: https://github.com/fpiikt/sum-of-two-Edites/

  Задача - "Сумма двух чисел":

  Для данного набора целых чисел, содержащихся в кортеже или списке,
  вернуть индексы двух таких чисел, что их сумма будет равна целевому числу
  (целочисленный тип данных), заданному в переменной target.

  Можно предположить, что каждый входной набор (список/кортеж и целое число)
  будет иметь ровно одно решение, элемент списка/кортежа не может быть использован дважды.

  Решение реализовано внутри метода find_sum
"""


def is_int(n):
    try:
        return float(n).is_integer()
    except ValueError:
        return False


def find_sum(numbers, target):
    if len(numbers) < 2:
        print("Не хватает элементов для выполнения задачи!")
        return -1

    for x in numbers:
        if not is_int(x):
            print("Введены некорректные значения элементов!")
            return -2

    if not is_int(target):
        print("Введено некорректное значение")
        return -1

    a_i = 0
    b_i = 0
    solves = []
    used_i = []
    numbers = list(map(float, numbers))
    target = int(float(target))

    for a_i in range(len(numbers)):
        for b_i in range(len(numbers)):
            if numbers[a_i]+numbers[b_i] == target and a_i not in used_i and b_i not in used_i and a_i != b_i:
                solves.append([a_i, b_i])
                used_i.append(a_i)
                used_i.append(b_i)

    if len(solves) < 1:
        print("С заданными параметрами решений нет!")
        return -3
    elif len(solves) > 1:
        print("С заданными параметрами существует несколько решений!")
        return -3
    else:
        print("Индексы элементов, соответствующие решению:", solves)
        return solves

numbers = input("Введите целые числа, разделенные пробелом:").split()
target = input("Введите целое число для суммы:")

find_sum(numbers, target)

assert find_sum([1,2,3,4,5,6,7,8,9], 6) == -3,
assert find_sum([1,2,3], 4) == [[0, 2]]
assert find_sum([100,1001,99,400], 500) == [[0, 3]]
assert find_sum([00,1,25,9,8.3], 17.3) == -2
assert find_sum([2,1,7,'s',8.3], 17.2) == -2
assert find_sum([4], 500) == -1
assert find_sum([1,2,3], 3) == [[0, 1]]