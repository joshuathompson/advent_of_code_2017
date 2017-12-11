programs = []
for line in open('./input.txt').readlines():
    parsed_line = line.rstrip().replace(',', '').split(' ')
    programs.append({
        'name': parsed_line[0],
        'weight': parsed_line[1].strip('()'),
        'children': [] if len(parsed_line) == 2 else parsed_line[3:]
    })

programs_with_children = [p for p in programs if len(p['children']) > 0]
names_of_programs_with_children = [p['name'] for p in programs_with_children]
names_of_programs_with_parent = []

for program in programs_with_children:
    names_of_programs_with_parent.extend(program['children'])

print(set(names_of_programs_with_children) - set(names_of_programs_with_parent))