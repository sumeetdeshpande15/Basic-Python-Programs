'''
Print the following pattern for the given N number of rows.

Pattern for N = 4

1
11
202
3003
'''

n = int(input())

# print(1)
# i = 1
# while i<n:
#     j = 0
#     while j<i+1:
#         if j==0 or j==i:
#             print(i, end='')
#         else:
#             print(0, end='')
#         j+=1
#     i+=1
#     print()


print(1)
for i in range(1,n):
    for j in range(i+1):
        if j==0 or j==i:
            print(i, end='')
        else:
            print(0, end='')
    print()