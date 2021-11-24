'''
Print the following pattern for the given number of rows.
Pattern for N = 4

   1
  232
 34543
4567654

The dots represent spaces.
'''

n = 4

for i in range(n):
    for j in range(1,n-i):
        print(' ', end='')

    for k in range(i+1):
        print(k+i+1, end='')

    for l in range(i):
        print(2*i-l, end= '')
    print()

'''
n = int(input())

currRow = 1

while currRow <=n:
    spaces = 1
    while spaces <= n-currRow:
        print(" ", end = '')
        spaces += 1

    currCol = 1
    valToPrint = currRow
    while currCol <= currRow:
        print(valToPrint, end='')
        valToPrint += 1
        currCol += 1

    currCol = 1
    valToPrint = 2*currRow - 2
    while currCol <= currRow - 1:
        print(valToPrint, end='')
        valToPrint -= 1
        currCol += 1

    print()
    currRow += 1
'''
