class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        head, tail = 0, n - 1

        while head < tail:
            s = numbers[head] + numbers[tail]

            if s == target:
                return [head + 1, tail + 1]
            elif s > target:
                tail -= 1
            else:
                head += 1
        return [-1, -1]