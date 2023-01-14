class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for index in range(len(s) // 2):
            temp = s[index]
            s[index] = s[len(s) - index - 1]
            s[len(s) - index - 1] = temp
        return
