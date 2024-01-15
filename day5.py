#Day 5:
#Question 16:
#Use a list comprehension to square each odd number in a list. 
#The list is input by a sequence of comma-separated numbers.

def func16():
    string = input('What is the list? ').split(',')
    ans = [int(num)**2 for num in string if int(num) % 2 == 1]
    return ans

#Question 17:
#Write a program that computes the net amount of a bank account
#based a transaction log from console input. The transaction log
#format is shown as following:
def func17():
    transactions = []
    while True:
        a = input()
        if a:
            transactions.append(a)
        else:
            break
    net_balance = 0
    print(x)
    for trans in transactions:
        a,b = trans.split(' ')
        if a == 'D':
            net_balance += int(b)
        else:
            net_balance -= int(b)
    return net_balance
        
