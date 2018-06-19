#
# Garrett Wayne
#

from linked_stack import *

# str -> float
# calculates the postfix order calculation of the expression, using stacks, returning the answer
def postfix_calc(ex):
    stack = empty_stack()
    inputs = ex.split()
    if len(inputs) == 1:
        return float(inputs[0])
    for a in inputs:
        if a == "+" or a == "-" or a == "*" or a == "/":
            op1, stack = pop(stack)
            op2, stack = pop(stack)
            if a == '+':
                stack = push(stack, (op2 + op1))
            elif a == '-':
                stack = push(stack, (op2 - op1))
            elif a == '*':
                stack = push(stack, (op2 * op1))
            elif a == '/':
                stack = push(stack, (op2 / op1))
        else:
            stack = push(stack, float(a))
    answer, stack = pop(stack)
    return answer
