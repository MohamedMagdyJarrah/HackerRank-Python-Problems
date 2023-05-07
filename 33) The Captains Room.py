# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
unordered_rooms = list(map(int,input().split()))
sorted_rooms = sorted(unordered_rooms)
for i in range(len(sorted_rooms)):
    if i < (len(sorted_rooms)-1):
        if sorted_rooms[i] != sorted_rooms[i-1] and sorted_rooms[i] != sorted_rooms[i+1]:
            print(sorted_rooms[i])
            break
    else:
        print(sorted_rooms[i])
         
#---------------------another code but consume time ---------------------------
K = int(input())
unordered_rooms = list(map(int,input().split()))

for i in range(len(unordered_rooms)):
    appeared=0
    appeared = unordered_rooms.count(unordered_rooms[i])
    if appeared == 1:
        print(unordered_rooms[i])
        break