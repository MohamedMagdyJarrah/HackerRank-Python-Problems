import re

pattern = re.compile(r'#[0-9a-fA-f]{3,6}')
bracket = False
N = int(input())
for i in range(N):
    line = input()
    if '{' in line:
        bracket = True
    elif '}' in line:
        bracket = False
    elif bracket:
        for color in re.findall(pattern,line):
            print(color)