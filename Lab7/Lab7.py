MAX_N = 13
dp = [[[0 for _ in range(MAX_N + 1)] for _ in range(MAX_N + 1)] for _ in range(MAX_N + 1)]

dp[1][1][1] = 1  # Базовый случай

for n in range(2, MAX_N + 1):
    for p in range(1, n + 1):
        for r in range(1, n + 1):
            dp[n][p][r] = dp[n-1][p-1][r] + dp[n-1][p][r-1] + (n - 2) * dp[n-1][p][r]

# Чтение и обработка входных данных
t = int(input())
for _ in range(t):
    n, p, r = map(int, input().split())
    print(dp[n][p][r])
