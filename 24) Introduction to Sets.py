def average(array):
    # your code goes here
    summ = sum(list(set(array)))
    avg = round(summ/len(list(set(array))),3)
    return avg
    
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)