

from collections import defaultdict


listA = [
    "Sparsh,Aishwarya,Abhay,Rohit",
    "Aishwarya,Amit,Jainisha",
    "Rohit,Suman,Animesh",
    "Pallav,Sparsh"
]

tree = defaultdict(list)    # dict to store parent and children (defaults to a list) 
all_children = set()

# Expected dictionary tree
# {
#     'Sparsh': ['Aishwarya', 'Abhay', 'Rohit'], 
#     'Aishwarya': ['Amit', 'Jainisha'], 
#     'Rohit': ['Suman', 'Animesh'], 
#     'Pallav': ['Sparsh']
# }

for entry in listA:
    members = entry.split(',')
    parent = members[0]
    children = members[1:]
    tree[parent].extend(children)
    all_children.update(children)


all_parents = set(tree.keys())  # get parents set from tree dict keys
roots = list(all_parents - all_children)  # There could be multiple roots

# Recursive function to print tree
def print_tree(node, level=0):
    print("----" * level + node)
    for child in tree.get(node, []):
        print_tree(child, level + 1)

# Print from each root
for root in roots:
    print_tree(root)