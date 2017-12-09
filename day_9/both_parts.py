characters = list(open("./input.txt").read())

i = 0
ignoreCharacters = False
depth = 1
points = 0
garbage_characters = 0
while i < len(characters) - 1:
    character = characters[i]

    if ignoreCharacters:
        if character == '!':
            i += 1
        elif character == '>':
            ignoreCharacters = False
        else:
            garbage_characters += 1
    else:
        if character == '<':
            ignoreCharacters = True
        elif character == '{':
            points += depth
            depth += 1
        elif character == '}':
            depth -= 1
    
    i += 1
    
print(points)
print(garbage_characters)