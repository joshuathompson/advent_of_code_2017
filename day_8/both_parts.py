import operator

operators = {
    '==': operator.eq,
    '>': operator.gt,
    '>=': operator.ge,
    '<': operator.lt,
    '<=': operator.le,
    '!=': operator.ne
}

registers = {}
highest = 0

for line in open('./input.txt').readlines():
    instructions = line.rstrip().split(" ")
    register = instructions[0]

    if register not in registers:
        registers[register] = 0

    if instructions[4] not in registers:
        registers[instructions[4]] = 0

    op = operators[instructions[5]]

    if op(registers.get(instructions[4]), int(instructions[6])):
        if instructions[1] == 'inc':
            registers[register] = registers[register] + int(instructions[2])
        else:
            registers[register] = registers[register] - int(instructions[2])

    maximum = max(registers, key=registers.get)

    if highest < registers[maximum]:
        highest = registers[maximum]


maximum = max(registers, key=registers.get)

print('final maximum: ' + str(registers[maximum]))
print('biggest at any point: ' + str(highest))

