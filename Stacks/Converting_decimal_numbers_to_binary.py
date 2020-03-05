from stack import Stack
from collections import deque
def digit_to_binary(number):
    the_stack = Stack()
    while number > 0:
        reminder = number % 2
        the_stack.push(reminder)
        number = number // 2
    reversed_digit = ''
    while not the_stack.isEmpty():
        reversed_digit = reversed_digit + str(the_stack.pop())
    return reversed_digit

print (digit_to_binary(44))
        
