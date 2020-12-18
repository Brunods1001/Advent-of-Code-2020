import re

with open('input.txt', 'r') as f:
    txt = f.read()


pwds = txt.split('\n')
pwds = [i for i in pwds if len(i) > 0]  # remove blank lines

num_passes = 0
for pwdi in pwds:
    xmin, xmax, letter, pwd = re.split('[:\s-]+', pwdi)
    xmin, xmax = int(xmin) - 1, int(xmax) - 1
    passes = (
        (pwd[xmin] == letter) ^ (pwd[xmax] == letter)
        )  # caret is XOR
    num_passes += passes

print('Number of passes:', num_passes)

