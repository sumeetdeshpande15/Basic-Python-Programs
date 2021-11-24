'''
Print the following pattern
Pattern for N = 4


*000*000*
0*00*00*0
00*0*0*00
000***000
'''
n = int(input())

i = 1
while i<=n:
    zero = 2
    while zero <= i:
        print(0, end='')
        zero += 1
    star = 1
    k = 1
    while star <= k:
        print('*', end='')
        star += 1
    zero1 = 1
    while zero1 <= n-i:
        print(0,end='')
        zero1+=1
    star1 = 1
    k1 = 1
    while star1 <= k1:
        print('*', end='')
        star1+=1
    zero2 = n
    while zero2 >= i+1:
        print(0, end='')
        zero2-=1
    star2 = n
    while star2 >= n:
        print("*", end='')
        star2 -= 1
    zero3 = 2
    while zero3 <=i:
        print(0, end='')
        zero3+=1
    print()
    i+=1

'''
n = int(input())

start = 1
end = 2*n+1
mid = n+1
row = 1
while row<=n:
    column = 1
    while column<=2*n+1:
        if column==start or column==end or column==mid:
            print("*",end='')
        else:
            print(0,end='')
        column = column+=1
    start = start+1
    end=end-1
    row+=1
    print()'''