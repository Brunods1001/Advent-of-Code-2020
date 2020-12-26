import sys

try:
    fname = sys.argv[1]
except IndexError:
    fname = 'input.txt'

with open(fname, 'r') as f:
    list_group = f.read().split('\n\n')

num_ans = 0
for group in list_group:
    group_ans = group.replace('\n', '')
    set_ans = set(group_ans)
    num_ans += len(set_ans)

print('The number of answers is', num_ans)
