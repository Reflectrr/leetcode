from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}
        for string in strs:
            chars = [0]*26
            for char in string:
                chars[ord(char)-ord('a')] += 1
            chars = tuple(chars)
            if chars in res:
                res[chars].append(string)
            else:
                res[chars]=[string]
        return list(res.values())
