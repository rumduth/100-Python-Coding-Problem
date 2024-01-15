#Day 16:
#Question 60:
#Write a program to compute:
#f(n)=f(n-1)+100 when n>0 and f(0)=0

def func60():
    n = int(input())
    if n == 0:
        return 0
    a = 0
    b = 0
    for i in range(1,n+1):
        b = a + 100
        a = b
    return b

#Question 61:
#The Fibonacci Sequence is computed based on the following formula:
#f(n)=0 if n=0
#f(n)=1 if n=1
#f(n)=f(n-1)+f(n-2) if n>1
#Please write a program to compute the value of f(n) with a given n input by console.

def func61():
    n = int(input())
    if n == 0 or n == 1:
        return n
    a = 0
    b = 1
    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
    return c

#Question 62:
#Similar to question 61, but we have to print the list of n terms in the sequence
def func62():
    n = int(input())
    my_list = []
    for i in range(0,n+1):
        if i == 0 or i == 1:
            my_list.append(i)
        else:
            my_list.append(my_list[i-1] + my_list[i-2])
    for i in range(n+1):
        my_list[i] = str(my_list[i])
    return ','.join(my_list)

#Question 63:
#Please write a program using generator to print the even numbers between 0 and n
#in comma separated form while n is input by console.
def my_generator(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

def func63():
    n = int(input('Number: '))
    my_list = []
    for i in my_generator(n):
        my_list.append(str(i))
    return ','.join(my_list)
    
#Question 64:
#Please write a program using generator to print the numbers which can be divisible
#by 5 and 7 between 0 and n in comma separated form while n is input by console.
def my_func64_generator(n):
    for i in range(n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

def func64():
    n = int(input('Number: '))
    my_list = []
    for i in my_func64_generator(n):
        my_list.append(str(i))
    return ','.join(my_list)
    
    
