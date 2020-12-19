with open('input.txt', 'r') as f:
    list_trees = f.read().splitlines()

x = y = 0
dx, dy = 3, 1
height = len(list_trees)
width = len(list_trees[0])

num_trees = 0
while y < height:
    obj = list_trees[y][x]
    print((x, y), obj)
    is_tree = obj == '#'
    num_trees += is_tree
    x = (x + dx) % width
    y += dy

print(num_trees)
