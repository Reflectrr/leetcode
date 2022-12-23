class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end, maxlength = -1, -1, 0
        for index in range(len(s)):
            # check for odd length
            left, right = index, index
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            length = right - left
            if length > maxlength:
                maxlength = length
                start = left
                end = right

            # check for even length
            left, right = index, index+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            length = right - left
            if length > maxlength:
                maxlength = length
                start = left
                end = right
        return s[start + 1 : end]
