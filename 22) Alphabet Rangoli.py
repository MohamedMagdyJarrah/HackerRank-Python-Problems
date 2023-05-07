def print_rangoli(size):
    # your code goes here
    alpha="abcdefghijklmnopqrstuvwxyz"[:size]
    for i in range(size-1 , -size,-1):
        i = abs(i)
        if i>=0:
            line = alpha[size:i:-1]+alpha[i:size]
            print("--"*i + "-".join(line)+ "--"*i)
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)