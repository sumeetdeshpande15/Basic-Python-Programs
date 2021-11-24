'''
Print the following pattern
Pattern for N = 4

   *
  ***
 *****
*******


The dots represent spaces.
'''

n = int(input())


for i in range(n):
    for j in range(1,n-i):
        print(' ', end='')
    
    for k in range(i+1):
        print('*', end='')

    for l in range(i):
        print("*", end = '')
    print()

'''
n = int(input())

currRow = 1

while currRow <= n:
    spaces = 1
    while spaces <= (n - currRow):
        print(" ", end = '')
        spaces += 1

    currCol = 1
    while currCol <= ((2*currRow) - 1):
        print("*", end = '')
        currCoc += 1
    print()
    currRow += 1
'''

