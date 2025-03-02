def process_field(n, m, field_num):
    field = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        s = list(input())
        for g in range(m):
            if s[g] == '*':
                field[i][g] = '*'
            else:
                field[i][g] = 0

    for i in range(n):
        for g in range(m):
            if field[i][g] == '*':
                for di in [-1, 0, 1]:
                    for dg in [-1, 0, 1]:
                        if di == 0 and dg == 0:
                            continue
                        ni, ng = i + di, g + dg
                        if 0 <= ni < n and 0 <= ng < m and field[ni][ng] != '*':
                            field[ni][ng] += 1

    print(f"Field #{field_num}:")
    for i in range(n):
        for g in range(m):
            if field[i][g] == '*':
                print('*', end='')
            else:
                print(field[i][g], end='')
        print()
    print()


def main():
    field_num = 1
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        process_field(n, m, field_num)
        field_num += 1


if __name__ == "__main__":
    main()