with open('./input.txt') as file:
    lines = [int(line.rstrip()) for line in file.readlines()]
    index = 0
    moves = 0
    offset = 0
    while index < len(lines):
        old_index = index
        offset = lines[index]
        index = lines[index] + index
        lines[old_index] = lines[old_index] - 1 if offset >= 3 else lines[old_index] + 1
        moves += 1

    print(moves)