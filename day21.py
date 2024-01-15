#Day 21
#Question 85:
#By using list comprehension, please write a program to print the list
#after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

def func85():
    my_list = [12,24,35,70,88,120,155]
    return [b for a,b in enumerate(my_list) if a not in [0,4,5]]

#Question 86:
#By using list comprehension, please write a program to print the
#list after removing the value 24 in [12,24,35,24,88,120,155].

def func86():
    my_list = [12,24,35,70,88,120,155]
    return [x for x in my_list if x != 24]
    

#Question 87:
#With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
#write a program to make a list whose elements are intersection of the above given lists.

def func87():
    a = set([1,3,6,78,35,55])
    b = set([12,24,35,24,88,120,155])
    return a.intersection(b)


#Question 88:
#With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list
#after removing all duplicate values with original order reserved.
def func88():
    my_list = [12,24,35,24,88,120,155,88,120,155]
    answer = []
    for i in my_list:
        if i not in answer:
            answer.append(i)
    return answer

#Question 89:
#Define a class Person and its two child classes: Male and Female. All classes have a method
#"getGender" which can print "Male" for Male class and "Female" for Female class.
class Person:
    def __init__(self,name):
        self.name = name
    def getGender(self):
        return 'Unknown'

class Male(Person):
    def __init__(self,name):
        Person.__init__(self,name)
        self.gender = 'Male'
    def getGender(self):
        return self.gender

class Female(Person):
    def __init__(self,name):
        Person.__init__(self,name)
        self.gender = 'Female'
    def getGender(self):
        return self.gender


