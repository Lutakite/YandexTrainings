num_people = int(input())
child_to_parent_dict = {}
number_of_chilren_dict = {}
all_children = set()
all_parents = set()
for i in range(num_people - 1):
    child, parent = input().split()
    child_to_parent_dict[child] = parent
    number_of_chilren_dict[parent] = number_of_chilren_dict.get(parent, 0) + 1
    all_children.add(child)
    all_parents.add(parent)

head = all_parents - all_children
cur_level_of_tree = all_children - all_parents - head
num_descendants = {name: 0 for name in cur_level_of_tree}
while cur_level_of_tree:
    next_level_of_tree = set()
    for name in cur_level_of_tree:
        parent = child_to_parent_dict[name]
        num_descendants[parent] = num_descendants.get(parent, 0) + num_descendants[name] + 1
        number_of_chilren_dict[parent] -= 1
        if number_of_chilren_dict[parent] == 0:
            next_level_of_tree.add(parent)
    cur_level_of_tree = next_level_of_tree
    cur_level_of_tree -= head

for name in sorted(num_descendants):
    print(name, num_descendants[name])