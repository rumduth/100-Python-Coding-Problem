#Day 9
#Question 26:
#Define a function with two numbers as arguments.
#You can compute the sum in the function and return the value.
def func26(num1, num2):
    return num1+num2

#Question 27:
#Define a function that can convert a integer into a string and print it in console.
def func27(num1):
    return str(num1)

#Question 28:
#Define a function that can receive two integer numbers in string form
#and compute their sum and then print it in console.

def func28(num1,num2):
    return int(num1) + int(num2)

#Question 29:
#Define a function that can accept two strings as input and
#concatenate them and then print it in console.
def func29(s1, s2):
    return s1+s2


#Question 30:
#Define a function that can accept two strings as input and print the string with
#maximum length in console. If two strings have the same length, then the function
#should print all strings line by line.
def func30(s1,s2):
    if len(s1) == len(s2):
        print(f'{s1}\n{s2}')
    elif len(s1) > len(s2):
        print(f'{s1}')
    else:
        print(f'{s2}')
