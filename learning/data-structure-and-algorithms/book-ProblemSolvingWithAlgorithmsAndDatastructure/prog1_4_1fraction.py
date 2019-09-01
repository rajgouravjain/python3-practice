class Fraction(object) :
    def __init__(self,num,den):
        self.num = num
        self.den = abs(den)

    def show(self):
        print(str(self.num) + "/" + str(self.den) )
    def __str__(self):
        return(str(self.num) + "/" + str(self.den))
    def __add__(self,other_fraction):
        new_num = (self.num * other_fraction.den) + (self.den * other_fraction.num)
        new_den = self.den * other_fraction.den
        gcd_of_num_den = gcd(new_num,new_den)
        return Fraction(new_num//gcd_of_num_den,new_den//gcd_of_num_den)

    def __sub__(self,other_fraction):
        new_num = (self.num * other_fraction.den) - (self.den * other_fraction.num)
        new_den = self.den * other_fraction.den
        gcd_of_num_den = gcd(new_num,new_den)
        return Fraction(new_num//gcd_of_num_den,new_den//gcd_of_num_den)


def gcd(m,n):

    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n


if  __name__ == '__main__' :
    f1 = Fraction(3,7)
    f2 = Fraction(4,5)
    print str(f1)
    print str(f2)
    f3 = f1 + f2
    print str(f3)
    f4 = f1 -f2
    print str(f4)
