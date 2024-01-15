#Day 18
import random
#Question 70:
#Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
def func70():
    my_list = [x for x in range(0,11) if x % 2 == 0]
    print(my_list)
    print("Random even number:",random.choice(my_list))

#Question 71:
#Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module
#and list comprehension.
def func71():
    my_list = [x for x in range(10,151) if x % 35 == 0]
    print(my_list)
    print("Random even number:",random.choice(my_list))

#Question 72:
#Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
def func72():
    my_list = []
    while len(my_list) != 5:
        x = int(random.uniform(100,200))
        if not x in my_list:
            my_list.append(x)
    return my_list

#Question 73:
#Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
def func73():
    my_list = []
    while len(my_list) != 5:
        x = int(random.uniform(100,200))
        if (not x in my_list) and (x % 2 == 0): 
            my_list.append(x)
    return my_list

#Question 74:
#Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
def func74():
    my_list = random.sample([x for x in range(1,1001) if x % 35 == 0],5)
    print(my_list)
