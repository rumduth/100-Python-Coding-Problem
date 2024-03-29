#Day 20

#Question 80:
#Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

def func80():
    my_list = [5,6,77,45,22,12,24]
    return [x for x in my_list if x % 2 == 1]

#Question 81:
#By using list comprehension, please write a program to print the list after removing numbers
#which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
def func81():
    my_list = [12,24,35,70,88,120,155]
    return [x for x in my_list if x % 35 == 0]

#Question 82:
#By using list comprehension, please write a program to print the list after removing the
#0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
def func82():
    my_list = [12,24,35,70,88,120,155]
    return [b for a, b in enumerate(my_list) if a % 2 == 1] 

#Question 83:
#By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].
def func83():
    my_list = [12,24,35,70,88,120,155]
    return [b for a, b in enumerate(my_list) if a not in range(2,5)] 

#Question 84:
#By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
def func84():
    matrix = []
    for i in range(3):
        matrix.append([])
        for j in range(5):
            matrix[i].append([])
            for k in range(8):
                matrix[i][j].append(0)
    return matrix

def func84_1():
    matrix = [[[0 for z in range(8)] for y in range(5)] for x in range(3)]
    return matrix
