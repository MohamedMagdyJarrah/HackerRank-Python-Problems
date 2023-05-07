def wrapper(f):
    def fun(l):
        # complete the function
        for i in range(len(l)):
            if len(l[i])==13:
                l[i] = l[i][:3] + ' ' + l[i][3:8] + ' ' + l[i][8:]
            elif len(l[i])==12:
                l[i] = l[i][:2] + ' ' + l[i][2:7] + ' ' + l[i][7:]
                l[i] = "+"+l[i]
            elif len(l[i])==11:
                l[i] = l[i][0] + ' ' + l[i][1:6] + ' ' + l[i][6:]
                l[i] = l[i].replace("0", "+91", 1)
            else:
                l[i] = l[i][:5] + ' ' + l[i][5:]
                l[i] = "+91 "+ l[i]
        f(l)
        
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


