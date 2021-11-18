'''
Print the following pattern for the given N number of rows.
Pattern for N = 4

A
BC
CDE
DEFG

'''

n = int(input())

for i in range(n):
    start_char = chr(ord('A') + i -1)  # kth char in alphabets
    for j in range(i+1):
        ans = chr(ord(start_char) + j + 1)
        print(ans, end='')
    print()


'''
n = int(input())

currRow = 1

while currRow <= n:
    currCol = 1

    ch = ord("A") + currCol - 1

    while currCol <= currRow:
        print(chr(ch + currCol - 1), end='')
        currCol += 1
    print()
    currRow += 1
'''