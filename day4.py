#Day 4

#Question 14
#Write a program that accepts a sentence and calculate
#the number of upper case letters and lower case letters.
def func14():
    sentence = input('What is your sentence? ')
    ans = {'Upper Case' : 0, 'Lower Case': 0}
    for letter in sentence:
        if letter >= 'a' and letter <= 'z':
            ans['Lower Case'] += 1
        elif letter >= 'A' and letter <= 'Z':
            ans['Upper Case'] += 1
        else:
            continue
    return ans


#Question 15
#Write a program that computes the value of a+aa+aaa+aaaa
#with a given digit as the value of a.

def func14():
    right_format = False
    while not right_format:
        sentence = input('What is the math? ')
        right_format = True
        for letter in sentence:
            if letter != 'a' and letter != '+':
                right_format = False
                break
            else:
                continue
    while True:
        try:
            digit = int(input('Digit for a: '))
        except:
            continue
        else:
            break
        
        
    numbers = sentence.split('+')
    ans = 0
    for num in numbers:
        num = int(num.replace('a',str(digit)))
        ans += num
    return ans
    
        
