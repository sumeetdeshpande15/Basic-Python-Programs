'''Print the following pattern for the given number of rows.
Note: N is always odd.


Pattern for N = 5

  *
 ***
*****
 ***
  *

The dots represent spaces.
'''

n = 7
n1 = n//2 + 1
n2 = n - n1

currRow = 1

while currRow <= n1:
    spaces = 1
    while spaces <= n1-currRow:
        print(" ", end = '')
        spaces += 1

    currCol = 1
    while currCol <= (2*currRow) - 1:
        print("*" , end = '')
        currCol += 1

    print()
    currRow += 1 

currRow = n2

while currRow >= 1:
    spaces = 1
    while spaces <= n2 - currRow + 1:
        print(" ", end = "")
        spaces += 1

    currCol = 1
    while currCol <= (2*currRow) - 1:
        print("*" , end="")
        currCol += 1

    print()
    currRow -= 1 


