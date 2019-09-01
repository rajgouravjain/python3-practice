from prog3_4_1_my_stack import Stack

def paranthesis_check(s1):
    """
        paranthesis_check("{}{]sdFGD{}{}{[}}")
    """
    s = Stack()
    balanced = True
    for c in s1:
        if c in "({[":
            s.push(c)
        elif c in ")}]":
            if s.isEmpty():
                balanced = False
            else :
                if matches(s.peek(),c):
                    s.pop()
                else:
                    balanced = False
                    s.pop()
        else :
            pass
    return balanced and s.isEmpty()

def matches(top,symbol):
    open_symbol = "([{"
    close_symbol = ")]}"

    return open_symbol.index(top) == close_symbol.index(symbol)


if  __name__ == "__main__":
    print(paranthesis_check("(sddsf{sdfdsf}{sdfdfd[sdsfdf]dfdfg}dffgdfg)dfgfdfg"))
    print(paranthesis_check("{}{]sdFGD{}{}{[}}"))
