import sys


class Elephant:
    def __init__(self, weight, iq, index):
        self.weight = weight
        self.iq = iq
        self.index = index


def read_input():
    elephants = []
    idx = 1
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        weight, iq = map(int, line.split())
        elephants.append(Elephant(weight, iq, idx))
        idx += 1
    return elephants


def sort_elephants(elephants):
    # Сортируем по возрастанию веса, а при одинаковом весе - по убыванию IQ
    return sorted(elephants, key=lambda x: (x.weight, -x.iq))


def find_longest_sequence(elephants):
    n = len(elephants)
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if (elephants[j].weight < elephants[i].weight and
                    elephants[j].iq > elephants[i].iq):
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

    max_length = max(dp)
    max_index = -1

    # Ищем слона с максимальной длиной и максимальным IQ
    for i in range(n):
        if dp[i] == max_length:
            if max_index == -1 or elephants[i].iq > elephants[max_index].iq:
                max_index = i

    return max_length, max_index, prev


def build_sequence(elephants, max_index, prev):
    sequence = []
    current = max_index
    while current != -1:
        sequence.append(elephants[current].index)
        current = prev[current]
    return sequence[::-1]


def main():
    elephants = read_input()
    elephants = sort_elephants(elephants)

    max_length, max_index, prev = find_longest_sequence(elephants)
    sequence = build_sequence(elephants, max_index, prev)

    print(max_length)
    for num in sequence:
        print(num)


if __name__ == "__main__":
    main()