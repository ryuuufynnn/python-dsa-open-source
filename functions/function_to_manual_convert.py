# Gumawa ng program na tatanggap ng sorted list of numbers at isang target number.
# Hanapin kung saang index unang lumabas ang target.
# Kung maraming beses lumabas ang target, ang pinakaunang occurrence lamang ang dapat ibalik.
# Kung hindi makita ang target, ibalik ang -1.
# Test Cases
# Input:
# Numbers: 1 2 2 2 4 5
# Target: 2
# Expected:
# 1

user_input = input("Enter a sorted list of numbers: ")
numbers = [int(x) for x in user_input.split()]

target = int(input("Enter a target number: "))

left = 0
right = len(numbers) -1
answer = -1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        answer = mid
        right = mid - 1
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print(answer)


# here's the function version:
# def first_occurrence(nums: list[int], target: int) -> int:
    # left = 0
    # right = len(nums) - 1
    # answer = -1

    # while left <= right:
    #     mid = (left + right) // 2

    #     if nums[mid] == target:
    #         answer = mid
    #         right = mid - 1
    #     elif nums[mid] < target:
    #         left = mid + 1
    #     else:
    #         right = mid - 1

    # return answer