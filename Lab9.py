from typing import List, Tuple, Set, Dict

# Направления для движения между клетками (dy, dx, from_part, to_part)
DIRECTIONS = [
    (-1, 0, 0, 2),  # верх
    (0, 1, 1, 3),  # право
    (1, 0, 2, 0),  # низ
    (0, -1, 3, 1),  # влево
]


class MazeSolver:
    def __init__(self, width: int, height: int, grid: List[str]):
        self.width = width
        self.height = height
        self.grid = grid
        self.visited = [[[False] * 4 for _ in range(width)] for _ in range(height)]
        self.cycle_count = 0
        self.max_cycle_length = 0

    def _is_valid_move(self, y: int, x: int) -> bool:
        """Проверяет, находится ли клетка в пределах лабиринта."""
        return 0 <= y < self.height and 0 <= x < self.width

    def _process_internal_transitions(self, y: int, x: int, part: int,
                                      stack: List[Tuple[int, int, int]]) -> None:
        """Обрабатывает внутренние переходы внутри клетки."""
        cell = self.grid[y][x]

        if cell == '/':
            transitions = {
                0: 3,  # верх → влево
                3: 0,  # влево → верх
                1: 2,  # право → низ
                2: 1  # низ → право
            }
        elif cell == '\\':
            transitions = {
                0: 1,  # верх → право
                1: 0,  # право → верх
                2: 3,  # низ → влево
                3: 2  # влево → низ
            }
        else:
            return

        new_part = transitions.get(part)
        if new_part is not None and not self.visited[y][x][new_part]:
            self.visited[y][x][new_part] = True
            stack.append((y, x, new_part))

    def _dfs(self, start_y: int, start_x: int, start_part: int) -> Tuple[int, bool]:
        """Выполняет поиск в глубину для обнаружения циклов."""
        stack = [(start_y, start_x, start_part)]
        self.visited[start_y][start_x][start_part] = True
        visited_parts: Set[Tuple[int, int, int]] = set()
        visited_cells: Set[Tuple[int, int]] = set()
        is_cycle = True

        while stack:
            y, x, part = stack.pop()
            visited_parts.add((y, x, part))
            visited_cells.add((y, x))

            # Обрабатываем внутренние переходы
            self._process_internal_transitions(y, x, part, stack)

            # Обрабатываем переходы к соседним клеткам
            for dy, dx, from_part, to_part in DIRECTIONS:
                if part == from_part:
                    ny, nx = y + dy, x + dx
                    if self._is_valid_move(ny, nx):
                        if not self.visited[ny][nx][to_part]:
                            self.visited[ny][nx][to_part] = True
                            stack.append((ny, nx, to_part))
                    else:
                        is_cycle = False

        return len(visited_cells), is_cycle

    def solve(self) -> Tuple[int, int]:
        """Находит все циклы в лабиринте и возвращает их количество и максимальную длину."""
        for y in range(self.height):
            for x in range(self.width):
                for part in range(4):
                    if not self.visited[y][x][part]:
                        length, is_cycle = self._dfs(y, x, part)
                        if is_cycle:
                            self.cycle_count += 1
                            self.max_cycle_length = max(self.max_cycle_length, length)
        return self.cycle_count, self.max_cycle_length


def main():
    """Основная функция для обработки ввода и вывода."""
    case_number = 1
    while True:
        width, height = map(int, input().split())
        if width == 0 and height == 0:
            break

        grid = [input().strip() for _ in range(height)]
        solver = MazeSolver(width, height, grid)
        count, longest = solver.solve()

        print(f"Maze #{case_number}:")
        if count == 0:
            print("There are no cycles.\n")
        else:
            print(f"{count} Cycles; the longest has length {longest}.\n")
        case_number += 1


if __name__ == "__main__":
    main()