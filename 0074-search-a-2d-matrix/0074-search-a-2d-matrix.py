class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        ans = False
        for i in range(n):
            if target in matrix[i]:
                ans=True
        return ans
        