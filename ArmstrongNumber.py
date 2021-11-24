'''
Write a Program to determine if the given number is Armstrong number or not. Print true if number is armstrong, otherwise print false.
An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.
For example,
371, as 3^3 + 7^3 + 1^3 = 371
1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634

Sample Input 1 :
1
Sample Output 1 :
true

Sample Input 2 :
103
Sample Output 2 :
false
'''


def checkArmstrong(num):
    n = [int(x) for x in num]
    count = 0
    for i in range(len(n)):
        count = count + n[i]**len(n)
    if count==int(num):
        return True
    else:
        return False

num = input()
if checkArmstrong(num):
    print('true')
else:
    print('false')


# def checkArmstrong(n):
#     digits = 0
#     num = n
#     while num>0:
#         digits += 1
#         num = //10
#     newNum = 0
#     num = n
#     while num>0:
#         last = num%10
#         newNum = newNum + (last**digits)
#         num = num//10
#     if(newNum == n):
#         return True
#     else:
#         return False

# n = int(input())
# if checkArmstrong(n):
#     print('true')
# else:
#     print('false')

