'''
Print the following pattern for the given number of rows.
Assume N is always odd.

Note : There is space after every star.

Pattern for N = 7

*
 * *
   * * *
     * * * *
   * * *
 * *
*
'''

n = int(input())

n1 = (n + 1)//2
n2 = n1-1

i = 1
while i <= n1:
    space = 1
    while space <= i-1:
        print(" ", end= '')
        space +=1 
    star = 1
    while star<=i:
        print("*",end=' ')
        star += 1
    print()
    i+=1

i = 1
while i<=n2:
    space = n2
    while space>=i+1:
        print(" ", end="")
        space -= 1
    star = n2
    while star>=i:
        print("*", end=" ")
        star-=1
    print()
    i+=1


# n = int(input())

# increasing = (n+1)//2
# decreasing = n - increasing

# i = 1
# while i <= increasing:

#     # printing spaces: 1st row has 0 spaces, 2nd row has 1 so ith will have i - 1 spaces
#     s = 1
#     while s <= i-1:
#         print(" ", end='')
#         s = s + 1
    
#     # printing stars: 1st row has 1 star, 2nd row has 2 and ith  row will have i stars
#     j = 1
#     while j <= i:
#         print("* ", end='')
#         j = j + 1
#     print()
#     i = i + 1

# i = 1
# while i <= decreasing:
#     s = 1
#     while s <= decreasing - i:
#         print(" ", end='')
#         s = s + 1

#     # printing stars 1st row has 3 star, 2nd row has 2 so ith will have decreasing - i + 1 stars
#     j = 1
#     while j <= decreasing - i + 1:
#         print("* ", end='')
#         j = j + 1
#     print()
#     i = i + 1
