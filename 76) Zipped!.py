# Enter your code here. Read input from STDIN. Print output to STDOUT
N,X = map(int,input().split())

sheet = []
for i in range(X):
    subject = list(map(float,input().split()))
    sheet.append(subject)
    
final_sheet = list(zip(*sheet))

for i in range(len(final_sheet)):
    print(sum(final_sheet[i])/X)