with open('input.txt', 'r') as f:
    list_trees = f.read().splitlines()

x = y = 0
dx, dy = 3, 1
height = len(list_trees)
width = len(list_trees[0])


def count_trees(list_trees, dx, dy):
    x = y = 0
    num_trees = 0
    while y < height:
        obj = list_trees[y][x]
        is_tree = obj == '#'
        num_trees += is_tree
        x = (x + dx) % width
        y += dy

    return num_trees


list_dxdy = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for i, (dx, dy) in enumerate(list_dxdy):
    print(f'Traversing slope {i} in direction: ({dx}, {dy})')
    num_trees = count_trees(list_trees, dx, dy)
    print(f'There are {num_trees} trees')
