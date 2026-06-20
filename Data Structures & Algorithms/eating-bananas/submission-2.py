import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ma = max(piles)
        mi = 0


        def check(x) -> bool:
            cnt = 0
            for p in piles:
                cnt += math.ceil(p / x)
            return cnt <= h
        while ma > mi:
            mid = (ma + mi) // 2
            res = check(mid)

            if res:
                ma = mid
            else:
                mi = mid
            
            if ma == mi:
                return ma
            if ma - mi == 1:
                return ma
        return ma
