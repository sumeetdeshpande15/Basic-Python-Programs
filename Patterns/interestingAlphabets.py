'''
Print the following pattern for the given number of rows.

Pattern for N = 5

E
DE
CDE
BCDE
ABCDE
'''


n = int(input())

for i in range(n):
    #k = n
    start_char = chr(ord('A') + n - i)
    for j in range(i+1):
        ans = chr(ord(start_char) + j - 1)
        print(ans, end="")
    #k-=1
    print()

'''
n = int(input())

currRow = 1

while currRow <= n:
    currCol = 1

    ch = ord("A") + n - currRow
    while currCol <= currRow:
        print(chr(ch + currCol - 1), end = '')
        currCol += 1
    print()
    currRow += 1
'''

