from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        # constrct the adjancy matrix
        adjancy = {}
        if beginWord not in wordList:
            wordList.append(beginWord)
        for word in wordList:
            # wildcard pattern for each word
            for index in range(len(word)):
                pattern = word[:index] + "*" + word[index + 1 :]
                if pattern not in adjancy:
                    adjancy[pattern] = [word]
                else:
                    adjancy[pattern].append(word)
        # BFS on adjancy matrix
        queue = deque([beginWord])
        visited = set()
        res = 1
        while queue:
            # append all neighbors into the queue
            for _ in range(len(queue)):
                word = queue.popleft()
                visited.add(word)
                for index in range(len(word)):
                    pattern = word[:index] + "*" + word[index + 1 :]
                    for neighbor in adjancy[pattern]:
                        if neighbor == endWord:
                            return res + 1
                        elif neighbor not in visited and neighbor not in queue:
                            queue.append(neighbor)
            res += 1
        return 0
