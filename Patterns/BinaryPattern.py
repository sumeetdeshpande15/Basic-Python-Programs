'''
Print the following pattern for the given number of rows.

Pattern for N = 4

1111
000
11
0
'''

n = int(input())

for i in range(n):
    for j in range(n-i):
        if i%2!=0:
            print(0, end='')
        else:
            print(1, end='')
    print()

'''
n = int(input())
for i in range(1, n+1):
    for j in range(1,n-i+2):
        if ((i%2)==1):
            print(1, end='')
        else:
            print(0, end='')
    print()
'''