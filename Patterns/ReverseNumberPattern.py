'''
Print the following pattern for the given N number of rows.
Pattern for N = 4

1
21
321
4321

'''


n = int(input())


for i in range(n):
    for j in range(i+1):
        print((i-j)+1, end=' ')
    print()

'''

n = int(input())

currRow = 1

while currRow <= n:
    currCol = currRow

    while currCol >= 1:
        print(currCol, end='')
        currCol -= 1
    print()
    currRow += 1

'''
