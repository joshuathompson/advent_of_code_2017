def spread_blocks(banks):
    current_largest_index = banks.index(max(banks))
    blocks_at_index = banks[current_largest_index]
    banks[current_largest_index] = 0
    spread_index = current_largest_index + 1 if current_largest_index != len(banks) - 1 else 0

    for _ in range(blocks_at_index):
        banks[spread_index] = banks[spread_index] + 1
        spread_index = spread_index + 1 if spread_index != len(banks) - 1 else 0

    return banks

banks = [int(bank) for bank in open('./input.txt').read().rstrip().split('\t')]
banks_history = []

while not banks in banks_history:
    banks_history.append(list(banks))
    banks = spread_blocks(banks)

print(len(banks_history))