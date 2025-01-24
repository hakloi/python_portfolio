class Fraction:
    
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            self.numer, self.denom = map(int, args[0].split('/'))
        elif len(args) == 2:
            self.numer, self.denom = args
        self.__simplify()
    
    def __gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)
    
    def __simplify(self):
        gcd = self.__gcd(self.numer, self.denom)
        self.numer = self.numer // gcd
        self.denom = self.denom // gcd
        return self

    def numerator(self, *args):
        if len(args):
            self.numer = args[0]
            self.__simplify()
        return self.numer

    def denominator(self, *args):
        if len(args):
            self.denom = args[0]
            self.__simplify()
        return self.denom 

    def __str__(self):
        return f"{self.numer}/{self.denom}"

    def __repr__(self):
        return f"Fraction({self.numer}, {self.denom})"
    