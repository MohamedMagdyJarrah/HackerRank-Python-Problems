from html.parser import HTMLParser

class MYHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print(tag)
        for ele in attrs:
            print("->",ele[0],">",ele[1])
    def handle_startendtag(self,tag,attrs):
        print(tag)
        for ele in attrs:
            print("->",ele[0],">",ele[1])


html = ""
for i in range(int(input())):
    html += input().strip()
    html += '\n'
    
parser = MYHTMLParser()
parser.feed(html)
parser.close()