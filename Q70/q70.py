class Solution:
    def climbStairs(self, n: int) -> int:
        l = [1,1,2]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for i in range(3,n+1):
                l.append(l[i-1]+l[i-2])
        return l[n]

print(Solution.climbStairs(4,4))
