def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    blocks = int(data[0])
    idx = 1

    for _ in range(blocks):
        idx += 1  # Пропускаем пустую строку
        participants = {}

        while idx < len(data) and data[idx].strip():
            parts = data[idx].split()
            if len(parts) < 4:
                idx += 1
                continue
            participant = int(parts[0])
            problem = int(parts[1])
            time = int(parts[2])
            status = parts[3].strip()  # Убираем лишние пробелы

            if participant not in participants:
                participants[participant] = {'solved': set(), 'penalty': 0, 'incorrect': {}}

            # Проверяем статус (учитываем как латинскую 'C', так и кириллическую 'С')
            if status in ['C', 'С']:  # Обрабатываем оба варианта
                if problem not in participants[participant]['solved']:
                    participants[participant]['solved'].add(problem)
                    participants[participant]['penalty'] += time
                    if problem in participants[participant]['incorrect']:
                        participants[participant]['penalty'] += 20 * participants[participant]['incorrect'][problem]
            elif status == 'I':
                if problem not in participants[participant]['solved']:
                    if problem not in participants[participant]['incorrect']:
                        participants[participant]['incorrect'][problem] = 0
                    participants[participant]['incorrect'][problem] += 1

            idx += 1

        # Подготовка данных для сортировки
        results = []
        for participant, info in participants.items():
            solved = len(info['solved'])
            if solved > 0:  # Выводим только тех, кто решил хотя бы одну задачу
                penalty = info['penalty']
                results.append((participant, solved, penalty))

        # Сортировка
        results.sort(key=lambda x: (-x[1], x[2], x[0]))

        # Вывод результатов
        for res in results:
            print(f"{res[0]} {res[1]} {res[2]}")

        if _ < blocks - 1:
            print()  # Пустая строка между блоками


if __name__ == "__main__":
    main()