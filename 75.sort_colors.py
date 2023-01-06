class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # BucketSort solution:
        # Time Complexity: O(n) two pass
        # Memory Complexity: O(1)
        # red, white, blue = 0, 0, 0
        # for num in nums:
        #     if num == 0:
        #         red += 1
        #     elif num == 1:
        #         white += 1
        #     elif num == 2:
        #         blue += 1
        # nums[:red] = [0] * red
        # nums[red : red + white] = [1] * white
        # nums[red + white :] = [2] * blue
        # return

        # QuickSort solution:
        # Time Complexity: O(n) one pass
        # Memory Complexity: O(1)

        left, right = 0, len(nums) - 1
        curr = 0
        while curr <= right:
            if nums[curr] == 0:
                temp = nums[left]
                nums[left] = 0
                nums[curr] = temp
                left += 1
            elif nums[curr] == 2:
                temp = nums[right]
                nums[right] = 2
                nums[curr] = temp
                right -= 1
                curr -= 1
            curr += 1
        return
