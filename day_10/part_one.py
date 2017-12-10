import operator
from functools import reduce

def knot_lengths(lengths, times=1):
    numbers = [i for i in range(256)]

    current_position = 0
    skip_size = 0
    for i in range(times):
        for length in lengths:
            subsection = numbers[current_position:current_position+int(length)]

            if current_position + int(length) > len(numbers):
                wrap_length = int(length) - len(subsection)
                wrap_subsection = numbers[0:wrap_length]

                reversed_combined_subsections = wrap_subsection[::-1] + subsection[::-1]

                numbers[current_position:] = reversed_combined_subsections[0:len(subsection)]
                numbers[0:wrap_length] = reversed_combined_subsections[len(subsection):]
            else:
                numbers[current_position:current_position+int(length)] = subsection[::-1] #non in-place alternative to reverse()


            current_position = ((current_position + int(length) + skip_size) % len(numbers))
            skip_size += 1

    return numbers

lengths = open("./input.txt").read().rstrip().split(",")

knotted_lengths = knot_lengths(lengths)
print(knotted_lengths[0] * knotted_lengths[1])

ascii_lengths = [ord(c) for c in open("./input.txt").read().rstrip()] + [17, 31, 73, 47, 23]
sparse_hash = knot_lengths(ascii_lengths, 64)

sparse_hash_groups = [sparse_hash[((i)*16):((i+1)*16)] for i in range(16)]
dense_hash = []

result = ''
for g in sparse_hash_groups:
    n = reduce(operator.xor, g)
    result += format(n, 'x')

print(result)
