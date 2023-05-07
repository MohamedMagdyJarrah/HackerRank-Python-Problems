def print_formatted(number):
    # your code goes here
    width_bin = len("{0:b}".format(number))
    for i in range(1,number+1):
        print("{0:>{1}d} {0:>{1}o} {0:>{1}X} {0:>{1}b}".format(i,width_bin))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)