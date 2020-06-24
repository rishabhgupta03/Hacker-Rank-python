def merge_the_tools(string, k):
    subsegment = len(string)/k
    for i in range(0,len(string),int(subsegment)):
        t=""
        for j in range(i,k+i):
            if string[j] in t:
                pass
            else:
                t=t+string[j]
        print(t)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
