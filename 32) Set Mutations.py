# Enter your code here. Read input from STDIN. Print output to STDOUT
num_A = int(input())
A = set(map(int,input().split()))
num_other = int(input())
for i in range(num_other):
    operation = input().split()
    other_set = set(map(int,input().split()))
    if "intersection_update" in operation:
        A.intersection_update(other_set)
    elif "symmetric_difference_update" in operation:
        A.symmetric_difference_update(other_set)
    elif "update" in operation:
        A.update(other_set)
    elif "difference_update" in operation:
        A.difference_update(other_set)
        
print(sum(list(A)))