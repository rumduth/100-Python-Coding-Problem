#Day 1:

#Question 1:Write a program which will find all such numbers
#which are divisible by 7 but are not a multiple of 5, between
#2000 and 3200 (both included).The numbers obtained should be
#printed in a comma-separated sequence on a single line.

def sol1(num1, num2):
    for i in range(num1,num2+1):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=' ')

#Question 2: Write a program which can compute the factorial of a
#given numbers.The results should be printed in a comma-separated
#sequence on a single line. Suppose the following input is supplied
#to the program: 8 Then, the output should be:40320

def sol2():
    num = int(input())
    if num == 0 or num == 1:
        return 1
    n = 1
    i = 2
    while i <= num:
        n = n*i
        i += 1
    return n


#Question 3: With a given integral number n, write a program to generate
#a dictionary that contains (i, i x i) such that is an integral number
#between 1 and n (both included).and then the program should print the dictionary.
#Suppose the following input is supplied to the program: 8

def sol3():
    n = int(input())
    my_dict = {key : key * key for key in range(1,n+1)}
    return my_dict
