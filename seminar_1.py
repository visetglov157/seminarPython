# Задание про число фибонначи
n = int(input('enter number: '))
n0 = 0
n1 = 0
n2 = 1
i = 2
while n0 < n:
    n0 = n1 + n2
    n1 = n2
    n2 = n0
    i += 1
    if n0 > n:
        i = 0

if i != 0:
    print(i)
else:
    print(-1)