'''
Print the following pattern for the given number of rows.

Pattern for N = 4

4444444
4333334
4322234
4321234
4322234
4333334  
4444444
'''

n = int(input())

k = (2*n)-1
low = 0
high = k-1
value = n
matrix = [[0 for i in range(k)] for j in range(k)]

for i in range(n):
    for j in range(low, high+1):
        matrix[i][j] = value
    for j in range(low+1, high+1):
        matrix [j][i] = value
    for j in range(low+1, high+1):
        matrix[high][j] = value
    for j in range(low+1, high):
        matrix[j][high] = value

    low += 1
    high -= 1
    value -= 1

for i in range(k):
    for j in range(k):
        print(matrix[i][j], end='')
    print()

# n = int(input())

# for i in range(1, n+1):
#     temp = n
#     for j in range(1, i):
#         print(temp, end='')
#         temp = temp - 1
#     for j in range(1, (2*n) - (2*i) + 2):
#         print(n-i+1, end='')
#     for j in range(1, i):
#         temp = temp + 1
#         print(temp, end='')
#     print()

# for i in range(n-1, 0, -1):
#     temp = n
#     for j in range(1, i):
#         print(temp, end='')
#         temp -= 1
#     for j in range(1, (2*n) - (2*i) + 2):
#         print(n-i+1, end='')
#     for j in range(1,i):
#         temp = temp + 1
#         print(temp, end='')
#     print()