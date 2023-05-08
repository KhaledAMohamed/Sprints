def isBalanced(balancedBrackets):
    #create stack to git in it the open prakets
    stack = []
    #create for loop to loop inside the string
    for bracket in balancedBrackets:
        #make if condition to check it the braket is oppen append it to the stack
        if bracket in ['(', '[', '{']:
            stack.append(bracket)
        # else this meain the braket is closed or something else
        else:
            #so in else we check it the last item in stak are the closed item in we git or not
            #if not this mean this breaket dont close so this string is un ballnced
            if not stack:
                return "NO"
            if bracket == ')' and stack[-1] == '(':
                stack.pop()
            elif bracket == ']' and stack[-1] == '[':
                stack.pop()
            elif bracket == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return "NO"
    if not stack:
        return "YES"
    else:
        return "NO"

print(isBalanced("{[(({}{}()))]}"))
