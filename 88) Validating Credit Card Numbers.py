import re

        
for i in range(int(input())):
   creditNo = input()
   if bool(re.match(r'\d{16}',creditNo)) or bool(re.match(r'(\d{4}-){3}\d{4}$',creditNo)):
       x = "".join(creditNo.split('-'))
       if bool(re.match(r'[456]\d{15}',x)) and not re.search(r'(.)\1{3}',x):
           print("Valid")
       else:
           print("Invalid")
   else:
        print("Invalid")
           