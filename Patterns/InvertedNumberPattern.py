'''
Print the following pattern for the given N number of rows.

Pattern for N = 4

4444
333
22
1
'''

n = int(input())

for i in range(n):
    for j in range(n-i):
        print(n-i, end='')
    print()

'''
n = int(input())

currRow = 1
while currRow <= n:
    currCol = 1

    while currCol <= (n-currRow + 1):
        print(n - currRow + 1, end = '')
        currCol += 1
    print()
    currRow += 1
'''