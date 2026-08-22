class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0 # start left
        right = len(nums) - 1 # start sa right o dulo

        while left <= right:
            mid = (left + right) // 2 # sa gitna mag sstart?

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

user_input = input("Numbers: ")
numbers = [int(x) for x in user_input.split()]

target = int(input("Target: "))

print(f"index: {Solution().searchInsert(numbers, target)}")

