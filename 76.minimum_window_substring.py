from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        resStart, resEnd = 0, 0
        minResStart, minResEnd = -1, -1  # result is [minResStart,minResEnd]
        minLength = len(s) + 1
        tCharMap = defaultdict(int)
        sCharMap = defaultdict(int)
        totalChar = len(t)
        usefulChar = 0

        for index in range(len(t)):
            tCharMap[t[index]] += 1

        for index in range(len(s)):
            char = s[index]
            if char in tCharMap:
                sCharMap[char] += 1
                if sCharMap[char] <= tCharMap[char]:
                    usefulChar += 1
            if usefulChar == totalChar:
                resEnd = index
                while resEnd > resStart:
                    if s[resStart] in sCharMap:
                        if sCharMap[s[resStart]] > tCharMap[s[resStart]]:
                            sCharMap[s[resStart]] -= 1
                        else:
                            sCharMap[s[resStart]] -= 1
                            usefulChar -= 1
                            break
                    resStart += 1
                length = resEnd - resStart + 1
                if length < minLength:
                    minLength = length
                    minResStart, minResEnd = resStart, resEnd
                resStart += 1
            # print('resStart, resEnd:', resStart, resEnd)
            # print('minResStart, minResEnd:', minResStart, minResEnd)
            # print('sCharMap:', sCharMap)
            # print('tCharMap:', tCharMap)
        return s[minResStart : minResEnd + 1] if minResStart != -1 else ""
