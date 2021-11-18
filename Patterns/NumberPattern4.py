'''
Print the following pattern for the given N number of rows.

Pattern for N = 4

1234
123
12
1
'''

n = 5
for i in range(n):
    for j in range(n-i):
        print(j+1,end='')
    print()

'''
n = int(input())
i = 0
while i<n:
    j = 1
    while j<n-i+1:
        print(j, end='')
        j+=1
    i += 1
    print()
'''