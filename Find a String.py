def count_substring(string, sub_string):
    sum = 0
    for i in range(len(string)):
        c= string[i:i+len(sub_string)]
        if c == sub_string:
            sum = sum + 1
    return sum

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)