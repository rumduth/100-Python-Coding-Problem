#Day 2

#Question 4: Write a program which accepts a sequence of comma-separated numbers
#from console and generate a list and a tuple which contains every number.
def func4(string):
    a = string.split(',')
    b = tuple(a)
    return a, b

#Question 5:
'''
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''
class Question5:
    def __init__(self):
        self.string = ' '
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string.upper())
        
#Question6:
'''
Write a program that calculates and prints the value
according to the given formula:
Q = Square root of [(2 _ C _ D)/H]
'''
import math
def func6(li):
    d = []
    li = li.split(',')
    for i in li:
        d.append(float(i))
    for i in range(len(d)):
        d[i] = str(int(math.sqrt(2 * 50 * d[i] / 30)))
    return ','.join(d)

#Question7:
'''
Write a program which takes 2 digits, X,Y as input and generates
a 2-dimensional array. The element value in the i-th row and j-th
column of the array should be i _ j.*
'''
def func7():
    i = int(input('Row: '))
    j = int(input('Col: '))
    result = [[0 for col in range(j)] for row in range(i)]
    for row in range(i):
        for col in range(j):
            result[row][col] = row * col

    return result

#Question 8:
'''
Write a program that accepts a comma separated sequence of words
as input and prints the words in a comma-separated sequence after
sorting them alphabetically.

'''
def func8():
    li = input("String: ").split(',')
    li.sort()
    return ','.join(li)

#Question 9:
'''
Write a program that accepts sequence of lines as input and prints the
lines after making all characters in the sentence capitalized.
'''
def func9():
    lines = []
    while True:
        s = input()
        if s:
            lines.append(s.upper())
        else:
            break
    return lines
        
