class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, maxLength = 0, 0, 0
        uniqueChar = set()
        while right < len(s):
            if s[right] not in uniqueChar:
                uniqueChar.add(s[right])
                maxLength = max(maxLength,right - left + 1)
            else:
                while s[left] != s[right]:
                    uniqueChar.remove(s[left])
                    left += 1
                left += 1
            right += 1
        return maxLength
