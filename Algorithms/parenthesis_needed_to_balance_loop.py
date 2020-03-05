def getMin(s):
    # Write your code here
    # parenthesis_state will increase by one when reaching left bracket and negative when reaching right bracket
    parenthesis_state = 0
    right_parenthesis_needed = 0
    left_parenthesis_needed = 0
    for i in range(len(s)):
        if(s[i] == '('):
            parenthesis_state += 1
        elif (s[i] == ')'):
            parenthesis_state += -1
        # parentheis_state will become -1 only if there was no left parenthesis before it hence we increase right_paren_needed
        # and reset the parenthesis state
        # this if statement will only account for the right unbalanced brackerts we also need to account for the left unbalanced after the loop finishes
        if(parenthesis_state == -1):
            right_parenthesis_needed += 1
            parenthesis_state = 0
    #the only way parenthesis_state will become positive is if left parenthesis is not followed by right_parenthesis
    left_parenthesis_needed = parenthesis_state
    return right_parenthesis_needed + left_parenthesis_needed
