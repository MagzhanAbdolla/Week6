def soyuzNeRushimih(a, b):
    listc = []
    d = a + b
    while d:
        listc.append(d.pop(d.index(min(d))))
    return listc
lista = list(map(int, input().split()))
listb = list(map(int, input().split()))
print(*soyuzNeRushimih(lista, listb))
