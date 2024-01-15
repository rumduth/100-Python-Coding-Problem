#Day 7
#Question 20:
#Define a class with a generator which can iterate the numbers,
#which are divisible by 7, between a given range 0 and n.

class my_generator:
    def __init__(self):
        self.max_value = int(input('What is the number? '))
    def generator(self):
        for i in range(self.max_value+1):
            if i % 7 == 0:
                yield i
    def action(self):
        for i in self.generator():
            print(i)


        
#Question 21:
#A robot moves in a plane starting from the original point (0,0).
#The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
#The trace of robot movement is shown as the following:
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
#Then, the output of the program should be: 2
import math
def func21():
    directions = {'horizontal' : 0, 'vertical': 0}
    while True:
        direction = input()
        if len(direction) == 0:
            break
        else:
            mov, value = direction.split(' ')
            if mov == 'UP':
                directions['vertical'] += int(value)
            elif mov == 'DOWN':
                directions['vertical'] -= int(value)     
            elif mov == 'RIGHT':
                directions['horizontal'] += int(value)
            else:
                directions['horizontal'] -= int(value)
    return int(math.sqrt(directions['horizontal']**2 + directions['vertical']**2))
