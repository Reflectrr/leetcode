class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        mid = (right - left) // 2
        while right >= left:
            if nums[mid] == target:
                return mid
            # left to mid is non-decreasing
            if nums[mid] >= nums[left]:
                # target might be in mid to right partition
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # mid to right i- non-decreasing
            else:
                if target < nums[mid] or target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            mid = (right - left) // 2 + left
        return -1
