# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

T = int(input())
for x in range(T):
    n = int(input())
    blocks =deque(map(int,input().split()))
    possible = True
    
    if blocks[0] >= blocks[-1]:
        max = blocks.popleft()
    else:
        max = blocks.pop()
    
    while len(blocks) != 0:

        if  len(blocks) == 1:
          if blocks[0] <= max:
            break
          else:
            possible = False
            break
        
        else:
          if (blocks[0] <= max and blocks[-1] <= max):
            if blocks[0] >= blocks[-1]: 
              max = blocks.popleft()
            else:
              max = blocks.pop()
          elif blocks[0] <= max:
            max = blocks.popleft()
          elif blocks[-1] <= max:
            max = blocks.pop()
          else:
            possible = False
            break

    if possible:
      print("Yes")
    else:
      print("No") 

