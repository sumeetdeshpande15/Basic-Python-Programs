'''
Print the following pattern for the given N number of rows.
Pattern for N = 4

*
**
***
****

'''
n = int(input())

for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()

"""
n = int(input())

currRow = 1

while currRow <= n:
    currCol = 1

    while currCol <= currRow:
        print("*", end = " ")
        currCol += 1

    print()
    currRow += 1 
"""
