# Enter your code here. Read input from STDIN. Print output to STDOUT
studentsEnglish = int(input())
rollEnglish = set(map(int,input().split()))
studentsFrench = int(input())
rollFrench = set(map(int,input().split()))

print(len(rollEnglish.symmetric_difference(rollFrench)))