S = input()

upper = []
lower = []
odd = []
even = []

for x in S:
    if x.isalpha():
        if x.isupper():
            upper.append(x)
        elif x.islower():
            lower.append(x)
    else:
        if int(x)%2 == 0:
            even.append(x)
        else:
            odd.append(x)
            
upper = sorted(upper)
lower = sorted(lower)
odd = sorted(odd)
even = sorted(even)

final = lower+upper+odd+even
final = "".join(final)
print(final)
