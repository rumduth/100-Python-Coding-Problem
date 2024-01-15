#Day 19
import random
#Question 75
#Please write a program to randomly print a integer number between 7 and 15 inclusive.

def func75():
    print(random.choice(range(7,15)))

#Question 76
#Please write a program to compress and decompress
#the string "hello world!hello world!hello world!hello world!".

from zlib import compress, decompress
def func76():
    msg = "hello world!hello world!hello world!hello world!"
    msg = msg.encode('utf-8')
    compress_msg = compress(msg)
    decompress_msg = decompress(compress_msg)
    print(f'Compress Message: {compress_msg}\nDecompress Message: {decompress_msg}')


#Question 77:
#Please write a program to print the running time of execution of "1+1" for 100 times.
from time import time

def func77():
    start = time()
    for i in range(100):
        x = 1 + 1
    end = time()
    print(f'The running time: {end - start}') 

#Question 78:
#Please write a program to shuffle and print the list [3,6,7,8].
def func78():
    my_list = [3,6,7,8]
    random.shuffle(my_list)
    print(my_list)

#Question 79:
#Please write a program to generate all sentences where subject is
#in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
def func79():
    subject = ['I','You']
    verb = ['Play','Love']
    obj = ['Hockey','Football']
    for i in subject:
        for j in verb:
            for k in obj:
                print(f'{i} {j} {k}')
