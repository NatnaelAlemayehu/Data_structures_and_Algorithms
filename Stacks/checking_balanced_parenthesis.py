from stack import Stack

def paren_comparision(paren, top_element):
    if paren == "(" and top_element == ")":
        return True
    elif paren == "{" and top_element == "}":
        return True
    elif paren == "[" and top_element == "]":
        return True  
    else:
        return False  

def parenthesis_checker(parenthesis):
    stack_object = Stack()
    is_balanced = True
    index = 0
    while index < len(parenthesis) and is_balanced:
        paren_character = parenthesis[index]
        if paren_character in '({[':
            stack_object.push(paren_character)
        elif paren_character in ')}]':
            if stack_object.isEmpty():
                is_balanced = False
            else:
                top_element = stack_object.pop()
                if not paren_comparision(top_element, paren_character):
                    is_balanced = False               
        index += 1
        
    if stack_object.isEmpty() and is_balanced:
        return True
    else:
        return False
    
print(parenthesis_checker("{{}}"))
