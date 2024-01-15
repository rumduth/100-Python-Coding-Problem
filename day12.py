#Day 12
#Question 44:
#Write a program which can map() to make a list whose elements are square of
#numbers between 1 and 20 (both included).

def func44():
    return list(map(lambda x:x**2, range(1,21)))

#Question 45:
#Define a class named American which has a static method called printNationality.

class American:
    @staticmethod
    def printNationality():
        print('I am American')

#Question 46:
#Define a class named American and its subclass NewYorker.

class NewYorker(American):
    pass
    
