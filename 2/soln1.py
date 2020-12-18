import re

with open('input.txt', 'r') as f:
    txt = f.read()


pwds = txt.split('\n')
pwds = [i for i in pwds if len(i) > 0]  # remove blank lines

num_passes = 0
for pwdi in pwds:
    xmin, xmax, letter, pwd = re.split('[:\s-]+', pwdi)
    letter_count = pwd.count(letter)
    passes = int(xmin) <= letter_count <= int(xmax)
    num_passes += passes

print('Number of passes:', num_passes)

