from itertools import groupby
S = input()

key_func = lambda x: x[0]

for key,group in groupby(S,key_func):
    num= int(key[0])
    rep = len(list(group))
    res = [rep,num]
    print(tuple(res),end=' ')