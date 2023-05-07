records=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([score,name])
records.sort()
#print(records)
seconed_loweset=0
for i in range(1,len(records)):
    if records[i][0] != min(records)[0]:
        seconed_loweset= records[i][0]
        break
#print(seconed_loweset)

names = []
for i in range(len(records)):
    if seconed_loweset in records[i]:
      names.append(records[i][1])
names.sort()
for name in names:
    print(name)