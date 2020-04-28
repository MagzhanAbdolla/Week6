def CountSort(list):
    Sortirovka = [0] * 101
    for i in list:
        Sortirovka[i] += 1
    for i in range(101):
        print((str(i) + ' ') * Sortirovka[i], end='')


list = [int(i) for i in input().split()]
CountSort(list)
