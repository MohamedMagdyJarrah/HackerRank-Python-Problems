from collections import OrderedDict
n = int(input())
words = OrderedDict()

for i in range(n):
    word = input()
    if word in words:
        words[word] = words[word]+1 
    else:
        words[word] = 1
        
items = list(words)
print(len(items))
for i in range(len(items)):
  print(words[items[i]],end=' ')


