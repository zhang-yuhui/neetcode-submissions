class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        edge = {}
        for i in prerequisites:
            to, fr = i[0], i[1]
            if to < numCourses:
                indeg[to] += 1
            if fr in edge:
                edge[fr].append(to)
            else:
                edge[fr] = [to]
        
        zero = set()
        for i in range(numCourses):
            if indeg[i] == 0:
                zero.add(i)
        ans = []
        while len(zero) > 0:
            x = zero.pop()
            ans.append(x)
            if x in edge:
                for i in edge[x]:
                    indeg[i] -= 1
                    if indeg[i] == 0:
                        zero.add(i)
                del edge[x]
        
        for i in range(numCourses):
            if indeg[i] > 0:
                return []
            elif indeg[i] < 0:
                print("!!!")
        
        return ans