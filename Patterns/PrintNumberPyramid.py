'''
Print the following pattern for a given n.

For eg. N = 6

123456
 23456
  3456
   456
    56
     6
    56
   456
  3456
 23456
123456
'''

n = 6

i = 0
while n>i:
    spaces = 1
    while spaces <= i:
        print(" ", end='')
        spaces += 1
    j = 1
    while n-i>=j:
        print(j+i, end="")
        j+=1
    i+=1
    print()

while i>1:
    spaces = 1
    while spaces<=i-2:
        print(" ", end='')
        spaces += 1
    j = n
    k = 1
    while j >= i-1:
        print(i+k-2, end = "")
        j-=1
        k+=1
    i-=1
    print()


# n = int(input())
# for i in range(1,n+1):
#     count = 1
#     for j in range(1, i):
#         print(" ", end="")
#         count+=1
#     num = i
#     for j in range(count, n+1):
#         print(num, end="")
#         num = num + 1
#     print()
# for i in range(n-1,0,-1):
#     count = 1
#     for j in range(1,i):
#         print(" ", end='')
#         count += 1
#     num = i
#     for j in range(count, n+1):
#         print(num, end='')
#         num+=1
#     print() 
