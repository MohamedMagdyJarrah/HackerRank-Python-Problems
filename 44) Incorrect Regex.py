# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
cases = int(input())
for i in range(cases):
    try:
        pattern = input()
        regex = re.compile(pattern)
        out = True
    except re.error:
        out = False
    print(out)