import re 

expression = r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])'

x = re.findall(expression,input(),re.IGNORECASE)

print(x)
if x:
    for i in x:
        print(i)
else:
    print(-1)