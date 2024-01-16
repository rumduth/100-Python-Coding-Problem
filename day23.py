#Day 23
#Question 95:
#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
#You are given scores. Store them in a list and find the score of the runner-up.
def func95():
    scores = [int(x) for x in input().split(' ')]
    max_score = -1
    runner_up = -1
    for s in scores:
        if max_score == -1:
            max_score = s
        elif max_score < s:
            runner_up, max_score = max_score, s
        elif max_score > s:
            if runner_up < s:
                runner_up = s
    return runner_up


#Question 96:
#You are given a string S and width W. Your task is to wrap the string into a paragraph of width.
def func96():
    msg = input()
    width = int(input())
    for i in range(0,len(msg),width):
        print(msg[i:i+width])
    
#Question 97:
#You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
import string
def func97():
    alphabet = string.ascii_lowercase
    ans = []
    n = int(input())
    lines = 2 * n - 1
    width = 4 * n - 3
    middle = int(width / 2)
    for i in range(int(lines/2)+ 1):
        line = ['-'] * width
        idx = n - 1 - i
        line[middle] = alphabet[idx]
        j = middle - 2
        k = middle + 2
        idx += 1
        while idx < n:
            line[j] = line[k] = alphabet[idx]
            j -= 2
            k += 2
            idx += 1
        ans.append(''.join(line))
    i = 1
    middle = int(lines/2)
    while len(ans) != lines:
        ans.append(ans[middle - i])
        i += 1
    matrix = '\n'.join(ans)
    return matrix

#Question 98:
#You are given a date. Your task is to find what the day is on that date.
import calendar
def func98():
    month, day, year = list(map(int, input().split(' ')))
    i_d = calendar.weekday(year, month,day)
    print(calendar.day_name[i_d].upper())

#Question 99:
#Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
#The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
def func99():
    input()
    a = set(map(int, input().split(' ')))
    input()
    b = set(map(int, input().split(' ')))
    c = a.symmetric_difference(b)
    c = sorted(c)
    for i in c:
        print(i)
    
