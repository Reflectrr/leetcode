class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = -1
        stack = []  # (index, height)
        for index in range(len(heights)):
            if not stack or heights[index] > stack[0][1]:
                stack.insert(0, (index, heights[index]))
            elif heights[index] < stack[0][1]:
                lastPos = index
                while stack and heights[index] < stack[0][1]:

                    length = index - stack[0][0]
                    area = length * stack[0][1]
                    if area > maxArea:
                        maxArea = area
                    lastPos = stack.pop(0)[0]
                stack.insert(0,(lastPos, heights[index]))
                
        for item in stack:
            length = len(heights) - item[0]
            area = length * item[1]
            if area > maxArea:
                maxArea = area
        return maxArea

