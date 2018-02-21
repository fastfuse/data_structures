from stack import Stack


def brackets_balanced(input_string):
    """
    Function to check brackets balance.

    :param input_string: input string w/ brackets.
    :return: bool
    """
    stack = Stack()
    balanced = True
    index = 0

    brackets = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    while index < len(input_string) and balanced:
        symbol = input_string[index]

        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                if stack.pop() != brackets.get(symbol):
                    balanced = False

        index = index + 1

    if balanced and stack.is_empty():
        return True
    else:
        return False

# ============================================================================


def to_binary(decimal_number):
    """
    Function to convert decimal number to binary.
    """
    remainings_stack = Stack()
    binary_string = "0b"

    while decimal_number > 0:
        rem = decimal_number % 2
        remainings_stack.push(rem)
        decimal_number = decimal_number // 2

    while not remainings_stack.is_empty():
        binary_string += str(remainings_stack.pop())

    return binary_string

# ============================================================================


def convert(decimal_number, base):
    """
    Function to convert decimal number to any base between 2 and 16.
    """
    digits = "0123456789ABCDEF"
    remainings_stack = Stack()
    converted_number = ""

    while decimal_number > 0:
        rem = decimal_number % base
        remainings_stack.push(rem)
        decimal_number = decimal_number // base

    while not remainings_stack.is_empty():
        converted_number += digits[remainings_stack.pop()]

    return converted_number

# ============================================================================


def infix_to_postfix(expression):
    """
    Function to convert expression in infix form to postfix form.
    """
    priorities = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }

    operands_stack = Stack()
    postfix_list = []
    token_list = expression.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            postfix_list.append(token)
        elif token == '(':
            operands_stack.push(token)
        elif token == ')':
            top_token = operands_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = operands_stack.pop()
        else:
            while (not operands_stack.is_empty()) and \
               (priorities[operands_stack.peek()] >= priorities[token]):
                postfix_list.append(operands_stack.pop())
            operands_stack.push(token)

    while not operands_stack.is_empty():
        postfix_list.append(operands_stack.pop())
    return " ".join(postfix_list)

# ============================================================================


def eval_postfix_expr(postfix_expression):
    """
    Function to evaluate postfix expression.
    """
    operands_stack = Stack()
    token_list = postfix_expression.split()

    for token in token_list:
        if token in "0123456789":
            operands_stack.push(int(token))
        else:
            operand2 = operands_stack.pop()
            operand1 = operands_stack.pop()
            result = do_math(token, operand1, operand2)
            operands_stack.push(result)

    return operands_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
