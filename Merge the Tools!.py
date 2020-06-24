def merge_the_tools(string, k):
    subsegment = int(len(string)/k)
    for i in range(subsegment):
        t=string[i*k:(i+1)*k]
        s=""
        for j in t:
            if j in s:
                pass
            else:
                s=s+j
        print(s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
