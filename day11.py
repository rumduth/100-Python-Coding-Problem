#Day 11:
#Question 38:
#With a given tuple (1,2,3,4,5,6,7,8,9,10),
#write a program to print the first half values
#in one line and the last half values in one line.

def func38():
    my_tuple = (1,2,3,4,5,6,7,8,9,10)
    print(f'First Half: {my_tuple[:5]}')
    print(f'Last Half: {my_tuple[5:]}')

#Question 39:
#Write a program to generate and print another tuple
#whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

def func39():
    my_tuple = tuple([x for x in range(1,11) if x % 2 == 0])
    print(my_tuple)

#Question 40:
#Write a program which accepts a string as input to print "Yes"
#if the string is "yes" or "YES" or "Yes", otherwise print "No".

def func40():
    in_put = input();
    if in_put in ['Yes','YES','yes']:
        print('Yes')
    else:
        print('No')


#Question 41:
#Write a program which can map() to make a list whose elements are
#square of elements in [1,2,3,4,5,6,7,8,9,10].

def func41():
    return list(map(lambda x: x*x, range(1,11)));

#Question 42:
#Write a program which can map() and filter() to make a list
#whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

def func42():
    my_map = list(map(lambda x : x*x, range(1,11)))
    my_list = list(filter(lambda x : x%2 == 0,my_map))
    return my_list

#Question 43:
#Write a program which can filter() to make a list whose elements
#are even number between 1 and 20 (both included).

def func43():
    return list(filter(lambda x : x%2 == 0,range(1,21)))
