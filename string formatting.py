import math
def print_formatted(number):
    width = len(bin(n).lstrip("0b"))
    for i in range(1, number + 1):
        d = str(i)
        a = hex(i).upper()
        h = a.lstrip('0X')
        o = oct(i).lstrip('0o')
        b = bin(i).lstrip("0b")
        print(d.rjust(width), o.rjust(width) ,h.rjust(width), b.rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)