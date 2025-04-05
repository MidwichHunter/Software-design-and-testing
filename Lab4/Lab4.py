from collections import defaultdict

def parse_record(line):
    parts = line.split()
    plate = parts[0]
    date_time = parts[1]
    _, day, hour, minute = map(int, date_time.split(':'))  # игнорируем месяц
    total_minutes = day * 24 * 60 + hour * 60 + minute
    action = parts[2]
    km = int(parts[3])
    return (plate, total_minutes, action, km, day, hour)


def process_block(rates, records):
    records.sort()  # сортируем по времени
    trips = defaultdict(list)

    for record in records:
        plate = record[0]
        trips[plate].append(record)

    result = {}

    for plate in trips:
        events = trips[plate]
        i = 0
        total_cost = 0
        while i < len(events) - 1:
            curr = events[i]
            next = events[i + 1]
            if curr[2] == "enter" and next[2] == "exit":
                km_diff = abs(curr[3] - next[3])
                rate = rates[curr[5]]  # час въезда
                trip_cost = km_diff * rate + 100  # 100 = $1.00
                total_cost += trip_cost
                i += 2
            else:
                i += 1
        if total_cost > 0:
            result[plate] = total_cost + 200  # $2.00 за счёт

    return result

def main():
    with open('input.txt') as f:
        input_lines = f.read().strip().split('\n')

    i = 0
    num_blocks = int(input_lines[i])
    i += 1

    output_blocks = []

    while i < len(input_lines):
        while i < len(input_lines) and input_lines[i].strip() == '':
            i += 1
        if i >= len(input_lines):
            break

        rates = list(map(int, input_lines[i].split()))
        i += 1

        records = []
        while i < len(input_lines) and input_lines[i].strip():
            records.append(parse_record(input_lines[i]))
            i += 1

        result = process_block(rates, records)
        output = []
        for plate in sorted(result):
            output.append(f"{plate} ${result[plate] / 100:.2f}")
        output_blocks.append('\n'.join(output))

    print('\n\n'.join(output_blocks))

if __name__ == "__main__":
    main()
