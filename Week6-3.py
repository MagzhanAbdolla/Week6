A, B = map(int, input().split())

RazmerPapki = sorted([int(input()) for _ in range(B)])
Kolichisnvo = sum(RazmerPapki)
while Kolichisnvo > A and B:
    Kolichisnvo = Kolichisnvo - RazmerPapki.pop()
    B = B - 1
print(B)
