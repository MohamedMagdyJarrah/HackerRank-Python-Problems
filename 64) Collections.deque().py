from collections import deque

queue = deque()

N = int(input())

for i in range(N):
    action = input().split()
    if len(action) == 2:
        num = int(action[1])   
    
    # print(action)

    if action[0] == "append":
        queue.append(num)
    if action[0] == "pop":
        queue.pop()
    if action[0] == "popleft":
        queue.popleft()
    if action[0] == "appendleft":
        queue.appendleft(num)
        
print(*list(queue))