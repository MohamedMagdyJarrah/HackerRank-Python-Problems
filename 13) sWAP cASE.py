def swap_case(s):
    modified = list(s) 
    for i in range(len(modified)):
        if modified[i].isupper():
           modified[i] = modified[i].lower()
        elif modified[i].islower():
           modified[i] = modified[i].upper()
    joined = "".join(modified)
    return joined

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
