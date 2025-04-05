def max_regions(n):
    if n < 2:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n == 4:
        return 8
    else:
        # Используем формулу: R(n) = 1 + C(n, 2) + C(n, 4)
        c2 = n * (n - 1) // 2
        c4 = n * (n - 1) * (n - 2) * (n - 3) // 24
        return 1 + c2 + c4

s = int(input())
for _ in range(s):
    n = int(input())
    print(max_regions(n))
