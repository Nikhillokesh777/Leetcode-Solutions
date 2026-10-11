class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for ch in columnTitle:
            result = result*26+(ord(ch)-ord('A')+1)
        return result