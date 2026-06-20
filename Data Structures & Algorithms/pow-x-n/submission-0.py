class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        neg = True if n < 0 else False

        n = -n if neg == True else n

        power = x
        res = 1
        while n != 0:
            
            if n % 2 == 1:
                res = res * power

            power = power * power
            n = n // 2
        
        if neg:
            res = 1 / res
        
        return res
