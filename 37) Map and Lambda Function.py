cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 1 :
        fib = [0]
    elif n == 0:
        fib=[]
    else:
        fib=[0,1]
        for i in range(2,n):
            adding = fib[i-2]+fib[i-1]
            fib.append(adding)
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))