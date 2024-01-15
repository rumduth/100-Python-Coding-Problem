#Day 17:
#Question 65:
#Please write assert statements to verify that every number in the list [2,4,6,8] is even.
def func65():
    my_list = [2,4,5,8]
    for i in my_list:
        assert i % 2 == 0, f'{i} is not an even number'
    
#Question 66:
#Please write a program which accepts basic mathematic expression from
#console and print the evaluation result.

def func66():
    print(eval(input()))
    
#Question 67:
#Please write a binary search function which searches an item in a sorted list.
#The function should return the index of element to be searched in the list.

def func67(my_list, ele):
    i = 0
    j = len(my_list) - 1
    while i <= j:
        m = int ((i + j) / 2)
        if my_list[m] == ele:
            return m
        elif my_list[m] > ele:
            j = m - 1
        else:
            i = m + 1
    return -1

#Question 68:
#Please generate a random float where the value is between 10 and 100 using Python module.
import random as rd
def func68():
    return rd.uniform(10,100)

#Question 69:
#Please generate a random float where the value is between 5 and 95 using Python module.
def func69():
    return rd.uniform(5,95)
