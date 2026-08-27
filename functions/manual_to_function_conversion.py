# Problem: Given a sorted list and a target, find the target’s last index, or return -1 if it is absent.
# Word Problem
# Gumawa ng program na tatanggap ng sorted list of numbers at isang target number.
# Hanapin ang pinakahuling index kung saan lumabas ang target.
# Kung maraming beses lumabas ang target, dapat ang last/rightmost occurrence ang ibalik.
# Kung hindi makita ang target, ibalik ang -1.
# Test Cases
# Test Case 1
# Numbers: 1 2 2 2 4 5
# Target: 2
# Expected: 3

def last_occurence(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) -1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            answer = mid
            left = mid + 1
            continue
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return answer

user_input = input("Enter a number: ")
nums = [int(x) for x in user_input.split()]

target = int(input("Enter a target: "))

print(last_occurence(nums, target))

# manual version
user_input = input("Enter a numbers: ")
nums = [int(x) for x in user_input.split()]
target = int(input("Enter a target: "))

left = 0
right = len(nums) -1
answer = -1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        left = mid + 1
        answer = mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid -1
print(answer)

# note: if sorted ang list or test cases okay ang while loop approach, pero kung ang list ay unasored ganito magiging approach:
# for x in range(len(nums) -1, -1, -1):
#     if nums[x] == target:
#         answer = x
#         break
# print(answer)