#!/usr/local/bin/python3
#: Title       : ItsMath
#: Date        : 2021-01-30
#: Author      : "Kjetil Kristoffer Solberg" <post@ikjetil.no>
#: Version     : 0.1
#: Description : math functionality
#: Usage       : import ItsMath
class ItsMath:
    @staticmethod
    def IsPrime(n):
        if n == 1:
            return True

        for i in range(2,n):
            if (n % i) == 0:
                return False
        return True

    @staticmethod
    def isEven(n):
        if (n % 2) == 0:
            return True
        return False
        
    @staticmethod
    def isOdd(n):
        if (n %2) != 0:
            return True
        return False