with open('./input.txt') as file:
    lines = [int(line.rstrip()) for line in file.readlines()]
    index = 0
    moves = 0
    while index < len(lines):
        old_index = index
        index = lines[index] + index
        lines[old_index] = lines[old_index] + 1
        moves += 1

    print(moves)