# Problem: Given a sorted list and target, find the target’s first index, or return -1 if absent.
def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) -1
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            answer = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return answer

user_input = input("Enter a numberss: ")
nums = [int(x) for x in user_input.split()]

target = int(input("Enter a target: "))

print(f'index: {search(nums, target)}')