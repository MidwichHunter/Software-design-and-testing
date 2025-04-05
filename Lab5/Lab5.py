def who_wins(n):
    turn = 0  # 0 — Stan, 1 — Ollie
    p = 1
    while p < n:
        if turn == 0:
            p *= 9
        else:
            p *= 2
        turn = 1 - turn
    return "Ollie wins" if turn == 0 else "Stan wins"

# Чтение входных данных из консоли
import sys

for line in sys.stdin:
    line = line.strip()
    if line:
        n = int(line)
        print(who_wins(n))
