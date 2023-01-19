#Implement a function that will flaten and sort an array of integers in ascending order
numbers_tuple = ((4,5,6), (8,12,16), (10,15,20))
result = sorted(sum(numbers_tuple, ()))

print("Original:", numbers_tuple)
print("flatten and ascending:", result)
#flatten and ascending list: (4, 5, 6, 8, 10, 12, 15, 16, 20)

#How does this solution ensure data immutability?
#By using a tuple

#Is this solution a pure function? Why or why not?
#No, because its output value doesnt follow solely from its input values

#Is this solution a higher order function? Why or why not?
#Yes, because it contains other functions as a parameter

#Would it have been easier to solve this problem using a different programming style?
#No

#Why in particular is functional programming a helpful paradigm when solving this problem?
#It simplifies something that is complex


#Object Oriented Prompt
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.condition = price
    
    def repair(self):
        self.condition = 'repaired'

class Anakins:
    def __init__(self, max_speed, condition, price):
        super.__init__(max_speed, condition, price)
    def boost(self):
        self.max_speed (*2)

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

def flame_jet(self, other):
    other.condition = 'trashed'


#How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
#Encapsulation
#Abstraction
#Inheritance
#Polymorphism
#The solution demonstrates encapsulation by having classes, if you use a class that is encapsulation.
#The solution demonstrates abstraction by using an abstract class as a blueprint for other classes.
#The solution demonstrates inheritance with AnakinsPod inheriting Podracer's parameters.
#The solution demonstrates polymorphism by having a class that inherits a condition from another class.

#Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
#No, OOP is the ideal method to use for problems like this, makes the code readable and understable.

