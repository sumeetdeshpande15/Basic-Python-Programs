'''
Print the following pattern for the given N number of rows.
Pattern for N = 4

4444
4444
4444
4444
'''

n = int(input())

for i in range(n):
    for j in range(n):
        print(n, end='')
    print()


'''
n = int(input())
currRow = 1

while currRow <= n:
    currCol = 1

    while currCol <= n:
        print(n, end='')
        currCol +1 1

    print()
    currRow += 1
'''