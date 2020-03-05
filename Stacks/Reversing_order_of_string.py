from stack import Stack
def reverse_string (argument):
    reversed_string = ''
    stack_object = Stack()
    for character in argument:
        stack_object.push(character)     
    while not stack_object.isEmpty():
        reversed_string = reversed_string + str(stack_object.pop())
    return True if argument == reversed_string else False
    
print(reverse_string("lol"))
