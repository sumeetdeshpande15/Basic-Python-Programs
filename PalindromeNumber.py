'''
Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121

Sample Input 1 :
121
Sample Output 1 :
true
'''

def checkPalindrome(num):
    rev = 0
    temp = num
    while num>0:
        a = num%10
        rev = rev*10 + a
        num = num//10
    if temp == rev:
        return True
    else:
        return False

num = int(input())
if checkPalindrome(num):
    print('true')
else:
    print('false')



# num = int(input())

# temp = num
# rev = 0

# while temp != 0:
#     rev = (rev*10) + (temp%10)
#     temp = temp // 10

# if num == rev:
#     print('true')
# else:
#     print('false')