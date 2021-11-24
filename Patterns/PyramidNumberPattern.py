'''Print the following pattern for the given number of rows.

Pattern for N = 4

   1
  212
 32123
4321234
'''

n = int(input())

i = 1

while i<=n:
    space = n
    while space>=i+1:
        print(" ", end='')
        space -= 1
    num = i
    while num!=0:
        print(num, end='')
        num -= 1
    j = 2
    while j<=i:
        print(j, end='')
        j += 1
    print()
    i+=1


# n = int(input())

# row = 1
# while(row<=n):
#     spaces = n-row
#     while spaces>0:
#         print(" ", end='')
#         spaces=spaces-1
#     value=row
#     while value>0:
#         print(value, end='')
#         value=value-1
#     value=value+2

#     while value<=row:
#         print(value, end='')
#         value=value+1
#     print()
#     row=row+1
