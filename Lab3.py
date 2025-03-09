def find_original_file(fragments):
    # Вычисляем длину оригинального файла
    total_length = sum(len(frag) for frag in fragments)
    num_files = len(fragments) // 2
    original_length = total_length // num_files

    # Перебираем все возможные пары осколков
    for i in range(len(fragments)):
        for j in range(i + 1, len(fragments)):
            # Пробуем объединить осколки в обоих порядках
            candidate1 = fragments[i] + fragments[j]
            candidate2 = fragments[j] + fragments[i]

            # Проверяем, подходит ли кандидат по длине
            if len(candidate1) == original_length:
                # Проверяем, можно ли из оставшихся осколков составить пары для candidate1
                if is_valid(candidate1, fragments):
                    return candidate1
            if len(candidate2) == original_length:
                # Проверяем, можно ли из оставшихся осколков составить пары для candidate2
                if is_valid(candidate2, fragments):
                    return candidate2
    return None

def is_valid(candidate, fragments):
    # Создаем словарь для подсчета осколков
    from collections import defaultdict
    frag_count = defaultdict(int)
    for frag in fragments:
        frag_count[frag] += 1

    # Удаляем осколки, которые уже использованы для создания кандидата
    frag1 = candidate[:len(candidate) // 2]
    frag2 = candidate[len(candidate) // 2:]
    if frag_count[frag1] == 0 or frag_count[frag2] == 0:
        return False
    frag_count[frag1] -= 1
    frag_count[frag2] -= 1

    # Пробуем объединить оставшиеся осколки в пары
    for frag in list(frag_count.keys()):
        while frag_count[frag] > 0:
            # Ищем парный осколок
            paired_frag = candidate[len(frag):] if frag == candidate[:len(frag)] else candidate[:len(frag)]
            if frag_count[paired_frag] == 0:
                return False
            frag_count[frag] -= 1
            frag_count[paired_frag] -= 1
    return True

def main():
    import sys
    input = sys.stdin.read().split('\n')
    idx = 0
    num_tests = int(input[idx].strip())
    idx += 1

    for _ in range(num_tests):
        # Пропускаем пустые строки
        while idx < len(input) and input[idx].strip() == '':
            idx += 1

        # Считываем осколки для текущего тестового блока
        fragments = []
        while idx < len(input) and input[idx].strip() != '':
            fragments.append(input[idx].strip())
            idx += 1

        # Находим оригинальную строку
        original = find_original_file(fragments)

        # Выводим результат
        print(original)
        print()

if __name__ == "__main__":
    main()