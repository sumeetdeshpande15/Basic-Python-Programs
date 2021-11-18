'''
Print the following pattern for the given N number of rows.

Pattern for N = 3
 
A
BB
CCC
'''

n = int(input())
for i in range(n):
    ch = chr(ord("A") + i - 1)
    for j in range(i+1):
        print(chr(ord(ch)+1), end='')
    print()

'''
n = int(input())

currRow = 1

while currRow <= n:
    currCol = 1

    ch = ord("A") + currRow - 1

    while currCol <= currRow:
        print(chr(ch), end='')
        currCol += 1
    print()
    currRow += 1 
'''
