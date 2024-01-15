#Day 15:
#Question 54:
#Assuming that we have some email addresses in the "username@companyname.com" format,
#please write program to print the company name of a given email address.
#Both user names and company names are composed of letters only.

import re
def func54():
    email = input('What are the emails? ')
    pattern = r'\w+@(\w+)\.com'
    companies = re.findall(pattern,email)
    print(companies)


#Question 55:
#Write a program which accepts a sequence of words separated by whitespace as input
#to print the words composed of digits only.

def func55():
    words = input('Input: ').split(' ')
    numbers = [e for e in words if e.isnumeric() == True]
    print(numbers)
    
#Question 56:
#Print a unicode string "hello world".

def func56():
    unicode_string = u'hello world'
    print(unicode_string)

#Question 57:
#Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
def func57():
    ascii_string = input()
    utf_8_string = ascii_string.encode('utf-8')
    print(utf_8_string)

#Question 58:
#Write a special comment to indicate a Python source code file is in unicode.
# -*- coding: utf-8 -*-

#Question 59:
#Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
def func59():
    n = int(input())
    a = 0
    b = 1
    ans = 0
    for i in range(n+1):
        ans += a/b
        a += 1
        b += 1
    print(round(ans,2))
