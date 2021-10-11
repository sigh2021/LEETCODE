from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        List = ["()"]
        if n == 1:
            return List
        if n>1:
            List = Solution.generateParenthesis(n-1,n-1)
            list = []
            len = n*2-2
            for str in List:
                #str = '('+str
                for i in range(0,len):
                    strNew = '('+str[0:i]+')'+str[i:len]
                    if list.count(strNew) == 0:
                        list.append(strNew)
            return list



list = Solution.generateParenthesis(3,3)
print(list)

