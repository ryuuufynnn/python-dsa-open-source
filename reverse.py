# user_input = input("Enter a numbers: ")
# numbers = [int(x) for x in user_input.split()]

# target = int(input("Enter a target: "))

# answer = -1
# left = 0
# right = len(numbers) -1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         right = mid - 1
#         answer = mid
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# print(f"index: {answer}")


# def first_occurence(numbers: list[int], target: int) -> int:
    
#     left = 0
#     right = len(numbers) -1
#     answer = -1

#     while left <= right:
#         mid = (left + right) // 2

#         if numbers[mid] == target:
#             answer = mid
#             right = mid - 1
#             break
#         elif numbers[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return answer

# user_input = input("Enter a numbers: ")
# numbers = [int(x) for x in user_input.split()]

# target = int(input("Enter a target: "))

# print(first_occurence(numbers, target))

def first_occurence(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) -1
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            answer = mid
            right = mid - 1
            break
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return answer

user_input = input("Enter a numbers: ")
nums = [int(x) for x in user_input.split()]

target = int(input("Enter a target: "))

print(first_occurence(nums, target))