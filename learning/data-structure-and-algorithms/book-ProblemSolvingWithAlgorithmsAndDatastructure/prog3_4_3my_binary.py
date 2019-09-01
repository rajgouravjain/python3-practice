from my_stack import Stack
class Digit():
    digits = "0123456789ABCDEF"
    def __init__(self,a):
        self.a = a
    def convert_to_base(self,base):
        decimal  = self.a
        s = Stack()
        while decimal > 0 :
            decimal, remender = divmod(decimal,base)
            s.push(remender)
        n = ""
        while not s.isEmpty() :
            n += Digit.digits[s.pop()]
        self.a = n
    def __str__(self):
        return self.a
if __name__ == "__main__":
    d = Digit(111)
    d.convert_to_base(16)
    print str(d)
