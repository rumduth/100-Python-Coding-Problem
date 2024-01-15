#Day 10

#Question 31:
#Define a function which can print a dictionary where the keys are
#numbers between 1 and 20 (both included) and the values are square of keys.
def func31():
    my_dict = {key : key*key for key in range(1,21)}
    for key, value in my_dict.items():
        print(f'{key} : {value}')

#Question 32:
#Define a function which can generate a dictionary where the keys are numbers
#between 1 and 20 (both included) and the values are square of keys.
#The function should just print the keys only.
def func32():
     my_dict = {key : key*key for key in range(1,21)}
     for key in my_dict.keys():
         print(key)

#Question 33
#Define a function which can generate and print a list where the values are
#square of numbers between 1 and 20 (both included).
def func33():
    my_list = [i*i for i in range(1,21)]
    print(my_list)

#Question 34:
#Define a function which can generate a list where the values are square of
#numbers between 1 and 20 (both included). Then the function needs to print
#the first 5 elements in the list.
def func34():
    my_list = [i*i for i in range(1,21)]
    print(my_list[0:5])

#Question 35:
#Define a function which can generate a list where the values are square of
#numbers between 1 and 20 (both included). Then the function needs to print
#the last 5 elements in the list.
def func35():
    my_list = [i*i for i in range(1,21)]
    print(my_list[(len(my_list)-5):])

#Question 36:
#Define a function which can generate a list where the values are square of
#numbers between 1 and 20 (both included). Then the function needs to print
#all values except the first 5 elements in the list.
def func36():
    my_list = [i*i for i in range(1,21)]
    print(my_list[5:])
    
#Question 37:
#Define a function which can generate and print a tuple where the value are
#square of numbers between 1 and 20 (both included).
def func37():
    my_tuple = [i*i for i in range(1,21)]
    my_tuple = tuple(my_tuple)
    print(my_tuple)
