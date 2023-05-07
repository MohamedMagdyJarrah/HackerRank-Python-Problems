def fun(s):
    # return True if s is ;a valid email, else return False
    try:
        username,link = s.split('@')
        website,extension = link.split('.')
    except ValueError:
        return False
    username = username.replace("_","").replace("-","")
    
    if username.isalnum() is False:
        return False
    elif website.isalnum() is False:  
        return False
    elif extension.isalpha() is False or len(extension) > 3:
        return False
    else:
        return True
    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)