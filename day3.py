#Question 10:
#Write a program that accepts a sequence of whitespace separated words as input and prints
#the words after removing all duplicate words and sorting them alphanumerically
def func10():
    string = sorted(list(set(input('What is your string? ').split(' '))))
    print(' '.join(string))  
    

#Question 11:
#Write a program which accepts a sequence of comma separated 4 digit binary numbers
#as its input and then check whether they are divisible by 5 or not. The numbers that
#are divisible by 5 are to be printed in a comma separated sequence.

def func11():
    binary_list = input('What are your binary numbers? ').split(',')
    for number in binary_list:
        n = int(number,2)
        if n % 5 == 0:
            print(f'{number} is divisible by 5')
        else:
            print(f'{number} is not divisible by 5')

#Question 12:
#Write a program, which will find all such numbers between 1000 and 3000 (both included)
#such that each digit of the number is an even number.The numbers obtained should be printed
#in a comma-separated sequence on a single line.

def check_even_digit(x):
    if x % 2 == 0:
        return True
    return False

def func12():
    a = int(input('From: '))
    b = int(input('To: '))
    for i in range(a,b+1):
        n = str(i)
        satisfied = True
        for j in range(len(n)):
            digit = int(n[j])
            if not check_even_digit(digit):
                satisfied = False
                break
        if satisfied:
            print(i,end=' ')
        
#Question 13:
#Write a program that accepts a sentence and calculate the number of letters and digits.

def pre_calculating(a):
    if (a >= 'a' and a <= 'z') or (a >= 'A' and a <= 'Z'):
        return ("letter")
    elif a >= '0' and a <= '9':
        return ("digit")
    else:
        return None
def func13():
    string = input("Input: ")
    letter = 0
    digit = 0
    for l in string:
        if pre_calculating(l) == 'letter':
            letter += 1
        elif pre_calculating(l) == 'digit':
            digit += 1
        else:
            continue
    print(f'LETTERS: {letter}\nDIGITS: {digit}')
