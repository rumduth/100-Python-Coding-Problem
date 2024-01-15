#Day 24:
#Question 100:
#You are given words. Some words may repeat. For each word, output its number of occurrences.
#The output order should correspond with the input order of appearance of the word.
def func100():
    n = int(input())
    my_dict = {}
    for i in range(n):
        x = input()
        if x not in my_dict.keys():
            my_dict[x] = 1
        else:
            my_dict[x] += 1
    print(len(my_dict))
    print([x for x in my_dict.values()])
        
    
#Question 101:
#You are given a string.Your task is to count the frequency of letters of the string
#and print the letters in descending order of frequency.
def func101():
    msg = input()
    my_dict = {}
    for i in msg:
        if i not in my_dict.keys():
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    a = list(my_dict.items())
    a.sort(key = lambda x : x[1], reverse = True)
    for x, y in a:
        print(f'{x} {y}')

#Question 102:
#Write a Python program that accepts a string and calculate the number of digits and letters.

def func102():
    msg = input()
    digits = 0
    letter = 0
    for c in msg:
        if c.isdigit():
            digits += 1
        elif c.isalpha():
            letter += 1
    print(f'Digits: {digits}\nLetters: {letter}')

#Question 103:
#Given a number N.Find Sum of 1 to N Using Recursion
def func103(n):
    if n == 0:
        return 0
    return n + func103(n-1)
