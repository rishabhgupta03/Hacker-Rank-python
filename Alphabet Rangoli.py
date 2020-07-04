import string
def print_rangoli(size):
    strings = string.ascii_lowercase
    l=[]
    for i in range(size):
        s = "-".join(strings[i:size])
        l.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    rangoli = "\n".join(l[::-1]+l[1:])
    print (rangoli)    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
