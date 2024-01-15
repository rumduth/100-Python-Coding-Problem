#Day 22
#Question 90:
#Please write a program which count and print the numbers of each character in a string input by console.
def func90():
    msg = input()
    my_dict = {}
    for i in msg:
        if i not in my_dict.keys():
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    for key, val in my_dict.items():
        print(f'{key}, {val}')
    
#Question 91:
#Please write a program which accepts a string from console and print it in reverse order.

def func91():
    msg = input()
    return msg[-1::-1]
        
#Question 92:
#Please write a program which accepts a string from console and print the characters that have even indexes.
def func92():
    msg = input()
    my_list = []
    for i in range(len(msg)):
        if i % 2 == 0:
            my_list.append(msg[i])
    return ''.join(my_list)
    

#Question 93:
#Please write a program which prints all permutations of [1,2,3]
from itertools import permutations
def func93():
    print(list(permutations([1,2,3])))

#Question 94:
#Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs'
#among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
def func94():
    max_count = int(94/4)
    chicken = 0
    rabbit = 0
    while rabbit <= max_count:
        chicken = 35 - rabbit
        if (chicken * 2 + rabbit * 4) == 94:
            print(f'Chicken: {chicken}\nRabbit: {rabbit}')
            return
        else:
            rabbit += 1
    print('Not possible')
