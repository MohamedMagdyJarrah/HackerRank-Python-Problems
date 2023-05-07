# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
numbers = set(map(int,input().split()))

commands = int(input())

while commands !=0:
    commands -=1
    instruction = input().split()
    if 'pop' in instruction :
        numbers.pop()
    elif 'remove' in instruction:
        numbers.remove(int(instruction[1]))
    elif 'discard' in instruction:
        numbers.discard(int(instruction[1]))
        
print(sum(list(numbers)))