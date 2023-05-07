N = int(input())
integers = list(map(int,input().split()))
integersPos = [element>0 for element in integers]

def isPalindrome(x):
  if list(str(x)) == list(reversed(str(x))):
    return True
  else:
    return False

# integers = [isPalindrome(element) for element in integers]
# print(integers)

if all(integersPos):
  integers = [isPalindrome(element) for element in integers]
  print(any(integers))

else:
  print(False)
