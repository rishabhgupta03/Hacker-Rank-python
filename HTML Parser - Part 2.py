from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self,data):
        if "\n"  not in data:
            print(">>> Single-line Comment" + "\n" + data)
        else:
            print(">>> Multi-line Comment" + "\n" + data)
    def handle_data(self,data):
        if data != ("\n"):
            print(">>> Data" + "\n" + data)
        else:
            pass  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
