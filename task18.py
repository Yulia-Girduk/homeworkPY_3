# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

N = abs(int(input('Введите количесто элементов в списке: ')))
listA = list()
for i in range(N):
    item = int(input('Введите значение элемента: '))
    listA.append(item)

X = int(input('Введите число X: '))
print("Список значений:")
print(listA)

index = 0
minNumber = abs(X - listA[index])

for i in range(1, len(listA)):
    minNumderI = abs(X - listA[i])
    if minNumderI < minNumber:
        minNumber = minNumderI
        index = i
print(f'К числу {X} самым близким по величине элементом является {listA[index]}.')