import math
from collections import Counter

programs = []
for line in open('./input.txt').readlines():
    parsed_line = line.rstrip().replace(',', '').split(' ')
    programs.append({
        'name': parsed_line[0],
        'weight': parsed_line[1].strip('()'),
        'children': [] if len(parsed_line) == 2 else parsed_line[3:]
    })

def calculate_tree_weight(node):
    program = [p for p in programs if p['name'] == node].pop()
    if len(program['children']) == 0:
        return int(program['weight'])
    else:
        return int(program['weight']) + sum([calculate_tree_weight(c) for c in program['children']])

root_node = [p for p in programs if p['name'] == 'dtacyn'].pop()
current_unbalance_difference = 0
source_of_unbalance_found = False
while not source_of_unbalance_found:
    weights = []
    for child in root_node['children']:
        weights.append(calculate_tree_weight(child))

    weight_distrubiton = Counter(weights).most_common()
    if len(weight_distrubiton) > 1:
        weight_of_normal = weight_distrubiton[0][0]
        weight_of_outlier = weight_distrubiton[len(weight_distrubiton)-1][0]
        index_of = weights.index(weight_of_outlier)
        root_node = [p for p in programs if p['name'] == root_node['children'][index_of]].pop()
        current_unbalance_difference = math.fabs(weight_of_normal - weight_of_outlier)
    else:
        print(root_node['name'])
        print(root_node['weight'])
        print('off by', int(current_unbalance_difference))
        source_of_unbalance_found = True