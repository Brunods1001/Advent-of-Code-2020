import sys

try:
    fname = sys.argv[1]
except IndexError:
    fname = 'input.txt'

with open(fname, 'r') as f:
    list_group = f.read().split('\n\n')

num_ans = 0
for group in list_group:
    list_ans = group.split()
    common_ans = None
    for ans in list_ans:
        if common_ans is None:
            common_ans = set(ans)
            continue
        common_ans = common_ans.intersection(ans)
    num_ans += len(common_ans)

print('The number of answers is', num_ans)
