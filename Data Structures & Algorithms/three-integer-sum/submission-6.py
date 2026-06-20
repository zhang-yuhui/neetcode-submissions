class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = dict()
        for i in nums:
            if i in s:
                s[i] += 1
            else:
                s[i] = 1
        n = len(nums)
        ans = set()
        for i in range(n-1):
            for j in range(i+1, n):
                x = nums[i]
                y = nums[j]
                s[x] -= 1
                s[y] -= 1
                #print(x, s[x], y, s[y])
                if (-(x+y)) in s and s[(-x-y)] > 0:
                    tmp = [x,y,-(x+y)]
                    tmp.sort()
                    ans.add((tmp[0], tmp[1], tmp[2]))
                s[x] += 1
                s[y] += 1
        ansarray = []
        for i in ans:
            ansarray.append([i[0], i[1], i[2]])
        return ansarray