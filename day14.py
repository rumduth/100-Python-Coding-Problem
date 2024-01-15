#Day 14
#Question 51
#Write a function to compute 5/0 and use try/except to catch the exceptions.

def func51():
    try:
        a = 5/0
        print(a)
    except ZeroDivisionError as error:
        print(error)
    except:
        print('other exception')
    else:
        print('Succesfully')

#Question 52:
#Define a custom exception class which takes a string message as attribute.

class Custom_Exception(Exception):
    def __init__(self, string):
        self.string = string

def func52():    
    num = int(input())

    try:
        if num < 5:
            raise Custom_Exception('Input is smaller than 5')
        elif num > 5:
            raise Custom_Exception('Input is greater than 5')
    except Custom_Exception as err:
        print("The error raisesd: " + err.message)

#Question 53:
#Assuming that we have some email addresses in the "username@companyname.com" format,
#please write program to print the user name of a given email address. Both user names
#and company names are composed of letters only.

def func53():
    emails = input('What are the emails? ').split(' ')
    for email in emails:
        print(email.split('@')[0],end=' ')
    
