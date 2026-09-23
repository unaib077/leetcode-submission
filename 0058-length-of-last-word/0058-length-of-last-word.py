class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s
        a = string.strip()
        b = a.split()
        length = len(b[-1])
        return length
        