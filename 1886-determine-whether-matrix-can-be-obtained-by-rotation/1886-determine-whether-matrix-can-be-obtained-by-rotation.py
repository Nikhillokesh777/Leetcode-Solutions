class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:

        for _ in range(4):
            if mat == target:
                return True
            n = len(mat)
            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            for row in mat:
                row.reverse()

        return False