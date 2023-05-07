N = int(input())
lst=[]
while (N != 0):
    N-=1
    command =input().split()
    if  'insert' in command: 
        lst.insert(int(command[1]),int(command[2]))
    elif 'print' in command:
        print(lst)
    elif 'remove' in command:
        lst.remove(int(command[1]))
    elif 'append' in command:
        #num = int(input())
        lst.append(int(command[1]))
    elif 'sort' in command:
        lst.sort()
    elif  'pop' in command:
        lst.pop()
    elif 'reverse' in command:
        lst.reverse()