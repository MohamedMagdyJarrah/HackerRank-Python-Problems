import re 

S = input()
k = input()
pattern = re.compile(k)
matched = pattern.search(S)

if not matched:
    print("(-1, -1)")

while matched:
    print("({0}, {1})".format(matched.start(),matched.end()-1))
    matched = pattern.search(S, matched.start() + 1)