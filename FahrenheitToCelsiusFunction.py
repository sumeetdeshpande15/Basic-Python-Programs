'''
Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.

Input Format :
3 integers - S, E and W respectively

Output Format :
Fahrenheit to Celsius conversion table. One line for every Fahrenheit and Celsius Fahrenheit value. Fahrenheit value and its corresponding Celsius value should be separate by tab ("\t")
'''

def printTable(start, end, step):
    while start <= end:
        cel = (start-32)*(5/9)
        print(start, int(cel), sep='\t')
        start += step


start, end, step = int(input()), int(input()), int(input())
printTable(start, end, step)


# def printTable(start, end, step):
#     currentValue = start
#     while currentValue <= end:
#         fValue = int((5/9)*(currentValue-32))
#         print(currentValue, end='\t')
#         print(fValue)
#         currentValue = currentValue + step

# s = int(input())
# e = int(input())
# step = int(input())
# printTable(s,e,step)