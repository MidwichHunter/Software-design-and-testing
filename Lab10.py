import sys
import heapq
from collections import defaultdict


def main():
    def read_input():
        """Читает весь ввод и возвращает список строк."""
        return sys.stdin.read().split('\n')

    def skip_empty_lines(input_lines, pointer):
        """Пропускает пустые строки и возвращает новый указатель."""
        while pointer < len(input_lines) and input_lines[pointer].strip() == '':
            pointer += 1
        return pointer

    def build_graph(input_lines, pointer, num_intersections):
        """Строит граф на основе входных данных."""
        graph = defaultdict(list)
        while pointer < len(input_lines):
            line = input_lines[pointer].strip()
            if line == '':
                pointer += 1
                continue
            if not all(x.isdigit() for x in line.split()):
                break
            u, v, w = map(int, line.split())
            graph[u].append((v, w))
            graph[v].append((u, w))
            pointer += 1
        return graph, pointer

    def compute_shortest_paths(graph, num_intersections):
        """Вычисляет кратчайшие пути между всеми парами вершин с помощью алгоритма Дейкстры."""
        INF = float('inf')
        dist = [[INF] * (num_intersections + 1) for _ in range(num_intersections + 1)]

        for source in range(1, num_intersections + 1):
            dist[source][source] = 0
            heap = [(0, source)]

            while heap:
                current_dist, u = heapq.heappop(heap)
                if current_dist > dist[source][u]:
                    continue

                for v, weight in graph[u]:
                    if dist[source][v] > current_dist + weight:
                        dist[source][v] = current_dist + weight
                        heapq.heappush(heap, (dist[source][v], v))

        return dist

    def find_optimal_depot(depots, dist, num_intersections):
        """Находит оптимальное место для нового депо."""
        INF = float('inf')

        # Вычисляем текущие минимальные расстояния
        min_dist = [INF] * (num_intersections + 1)
        for u in range(1, num_intersections + 1):
            for depot in depots:
                if dist[depot][u] < min_dist[u]:
                    min_dist[u] = dist[depot][u]

        # Ищем лучшее место для нового депо
        best_max_distance = INF
        best_location = 1

        for candidate in range(1, num_intersections + 1):
            temp_dist = min_dist.copy()

            for u in range(1, num_intersections + 1):
                if dist[candidate][u] < temp_dist[u]:
                    temp_dist[u] = dist[candidate][u]

            current_max = max(temp_dist[1:num_intersections + 1])

            if (current_max < best_max_distance or
                    (current_max == best_max_distance and candidate < best_location)):
                best_max_distance = current_max
                best_location = candidate

        return best_location

    # Основная логика программы
    input_lines = read_input()
    ptr = 0
    T = int(input_lines[ptr])
    ptr += 1

    for case in range(T):
        # Пропускаем пустые строки
        ptr = skip_empty_lines(input_lines, ptr)
        if ptr >= len(input_lines):
            break

        # Читаем количество депо и перекрестков
        num_depots, num_intersections = map(int, input_lines[ptr].split())
        ptr += 1

        # Читаем местоположения депо
        depots = []
        for _ in range(num_depots):
            ptr = skip_empty_lines(input_lines, ptr)
            if ptr >= len(input_lines):
                break
            depots.append(int(input_lines[ptr]))
            ptr += 1

        # Строим граф
        graph, ptr = build_graph(input_lines, ptr, num_intersections)

        # Вычисляем кратчайшие пути
        dist = compute_shortest_paths(graph, num_intersections)

        # Находим оптимальное местоположение для нового депо
        optimal_location = find_optimal_depot(depots, dist, num_intersections)

        # Выводим результат
        print(optimal_location)
        if case < T - 1:
            print()


if __name__ == "__main__":
    main()