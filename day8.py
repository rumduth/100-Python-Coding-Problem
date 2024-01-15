#Day 8
#Question 22
#Write a program to compute the frequency of the words from the input.
#The output should output after sorting the key alphanumerically.

from collections import Counter
def func22():
    words = input('What is the sentence? ').split(' ')
    my_words = []
    for word in words:
        my_words.append(word)
    my_words.sort()
    info = Counter(my_words)
    for key,value in info.items():
        print(f'{key}:{value}')

#Question 23 and 24
#Please write a program to print some Python built-in functions documents,
#such as abs(), int(), raw_input(). And add document for your own function
#Write a method which can calculate square value of number
def func23(num):
    '''
    It helps to return the square value of input number
    '''
    return num**2

print(func23.__doc__)


#Question 25:
#Define a class, which have a class parameter and have a same instance parameter.

class my_class:
    name = 'Thong'
    def __init__(self, name=None):
        self.name = name
