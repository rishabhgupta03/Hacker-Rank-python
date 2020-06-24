def minion_game(string):
    stuart = 0
    kevin = 0
    for i in range(len(s)):
        if s[i] in ['A','E','I','O','U']:
            kevin = kevin+(len(s)-i)
        else:
            stuart = stuart + (len(s)-i)
    if stuart > kevin:
        print(f'Stuart {stuart}')
    elif kevin > stuart:
        print(f'Kevin {kevin}')
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
