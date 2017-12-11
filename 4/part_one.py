with open('./input.txt') as file:
    number_of_valid_passphrases = 0
    for line in file.readlines():
        passphrases = line.rstrip().split(' ')
        if len(set(passphrases)) == len(passphrases):
            number_of_valid_passphrases += 1
    print(number_of_valid_passphrases)