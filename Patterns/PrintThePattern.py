'''
Print the following pattern for the given number of rows.

Pattern for N = 5

1    2   3    4   5
11   12  13   14  15
21   22  23   24  25
16   17  18   19  20
6    7    8   9   10
'''

n = int(input())
n1 = (n+1)//2
n2 = n - n1

for i in range(n1):
    for j in range(1, n+1):
        print(2*n*i+j, end=' ')
    print()

for i in range(n2, 0, -1):
    for j in range(1, n+1):
        print(n*(2*i-1)+j, end=' ')
    print()


# n = int(input())

# startValue = 1
# for i in range(1, n+1):
#     for j in range(startValue, startValue + n):
#         print(j ,end=' ')
#     print()
#     if (i==((n+1)//2)):
#         if ((n%2) != 0):
#             startValue = n*(n-2)+1
#         else:
#             startValue = n*(n-1)+1
#     elif((i>(n+1)//2)):
#         startValue = startValue - 2*n
#     else:
#         startValue = startValue + 2*n