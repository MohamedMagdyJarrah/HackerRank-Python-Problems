import re 
T = int(input())
pattern = re.compile(r'^[+-]?[0-9]*\.[0-9]+$')
for i in range(T):
    num = input()
    match = pattern.match(num)
    
    print(bool(match))