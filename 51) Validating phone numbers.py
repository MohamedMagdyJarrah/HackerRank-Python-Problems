# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for i in range(int(input())):
    number = input()
    if len(number) ==10 and number.isdigit():
        out = re.match(r"^[789]\d{9}$",number)
        if out:
            print("YES")
        else :
            print("NO")
    else:
        print("NO")  