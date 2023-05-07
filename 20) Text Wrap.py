import textwrap

def wrap(string, max_width):
    wrapped = ''
    for i in range(0,len(string),max_width):
        if (i+max_width) < len(string):
            wrapped +=string[i:i+max_width] +'\n'
        else:
            wrapped += string[i:i+max_width]     
    return wrapped

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)