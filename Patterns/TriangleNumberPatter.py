'''
Print the following pattern for the given N number of rows.
Pattern for N = 4

1
22
333
4444

'''

n = int(input())

num = 1
for i in range(n):
    for j in range(i+1):
        print(num, end='')
    num += 1
    print()


'''
n = int(input())

currRow = 1

while currRow <= n:
    currCol = 1

    while currCol <= currRow:
        print(currRow, end = '')
        currCol += 1
    print()
    currRow += 1
'''