def NKVD():
    n = int(input())
    a = map(int, input().split(maxsplit=n))
    print(*sorted(a))


print(NKVD())
