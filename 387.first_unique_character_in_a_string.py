class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hashmap = collections.defaultdict(int)
        for char in s:
            hashmap[char] += 1
        for index in range(len(s)):
            if hashmap[s[index]] == 1:
                return index
        return -1
