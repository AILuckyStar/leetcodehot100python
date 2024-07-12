class Solution:
    def binaryfindleft(self, nums, target):
        left, right = 0, len(nums) - 1
        leftBorder = -2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                leftBorder = right
        return leftBorder

    def binaryfindright(self, nums, target):
        left, right = 0, len(nums) - 1
        rightBorder = -2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
                rightBorder = left
            else:
                right = mid - 1
        return rightBorder

    def searchRange(self, nums, target):
        leftBorder = self.binaryfindleft(nums, target)
        rightBorder = self.binaryfindright(nums, target)
        if leftBorder == -2 or rightBorder == -2:
            return [-1, -1]
        if nums[leftBorder + 1] == target:
            return [leftBorder + 1, rightBorder - 1]
        return [-1, -1]


nums = [5, 7, 7, 8, 8, 10]
target = 8
S = Solution()
print(S.searchRange(nums, target))
