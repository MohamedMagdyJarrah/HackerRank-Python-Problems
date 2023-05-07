# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
import email.utils

for i in range(int(input())):
    name,address = input().split()
    out  = re.match(r"<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>",address)
    if out:
        #print(email.utils.formataddr((name,address)))
        print(name,address)