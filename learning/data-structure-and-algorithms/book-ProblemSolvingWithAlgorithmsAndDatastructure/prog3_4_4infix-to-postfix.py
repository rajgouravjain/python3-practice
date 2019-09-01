from prog3_4_1my_stack import Stack
import string
postfix_list = []
def infix_to_postfix(infix_expr):
    token_list = list(infix_expr)
    postfix_stack = Stack()
    for i in token_list:
        if i in string.ascii_letters or i in string.digits :
            postfix_list.append(i)
        elif i == "(":
            postfix_stack.push(i)

        elif i == ")":
            postfix_list.append(postfix_stack.pop())
            while postfix_stack.peek() != "("
                postfix_list.appen(postfix_stack.pop())
            postfix_stack.pop()

        else:
            while (not postfix_stack.isEmpty() or )
