'''
Print the following pattern for the given N number of rows.

Pattern for N = 4

****
***
**
*
'''

n = int(input())

for i in range(n):
    for j in range(n-i):
        print('*', end='')
    print()