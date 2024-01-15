#Day 6
#Question 18:
#A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
#Following are the criteria for checking the password:
#At least 1 letter between [a-z]
#At least 1 number between [0-9]
#At least 1 letter between [A-Z]
#At least 1 character from [$#@]
#Minimum length of transaction password: 6
#Maximum length of transaction password: 12
#Your program should accept a sequence of comma separated passwords and
#will check them according to the above criteria. Passwords that match
#the criteria are to be printed, each separated by a comma.

import re
def check_pass_validity(password):
    if len(password) < 6 or len(password) > 12:
        return False
    lower_letter = False
    number = False
    upper_letter = False
    special_character = False
    for letter in password:
        if letter >= 'a' and letter <= 'z':
            lower_letter = True
        elif letter >= 'A' and letter <= 'Z':
            upper_letter = True
        elif letter in ['$','#','@']:
            special_character = True
        elif letter >= '0' and letter <= '9':
            number = True
        else:
            return False
    return lower_letter and number and upper_letter and special_character
def func18():
    passwords = input().split(',')
    for password in passwords:
        if check_pass_validity(password):
            print(password)


#Question 19:
#You are required to write a program to sort the (name, age, score) tuples
#by ascending order where name is string, age and score are numbers.
#The tuples are input by console. The sort criteria is:
#1: Sort based on name
#2: Then sort based on age
#3: Then sort by score
#The priority is that name > age > score.

def func19():
    people = []
    while True:
        person = input()
        if len(person):
            info = person.split(',')
            people.append({'name': info[0],'age': info[1], 'score' : info[2]})
        else:
            break
    people.sort(key = lambda x : (x['name'],x['age'],x['score']))
    return people
                                            
                                
