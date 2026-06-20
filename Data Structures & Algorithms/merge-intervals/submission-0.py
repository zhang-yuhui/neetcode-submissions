class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))

        ans = [[intervals[0][0], intervals[0][1]]]
        n = len(intervals)
        for i in range(1, n):
            now = ans[-1]
            ne = intervals[i]
            if ne[0] <= now[1]:
                now[1] = max(now[1], ne[1])
            else:
                ans.append([ne[0], ne[1]])

        return ans