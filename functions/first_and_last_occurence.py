# def last_occurence(nums: list[int], target: int) -> int:
#     answer = -1s

#     for x in range(len(nums)):
#         if nums[x] == target:
#             answer = x
#     return answer
# user_input = input("Enter nums: ")
# numbers = [int(x) for x in user_input.split()]

# target = int(input("Enter your target: "))

# print(last_occurence(numbers, target))


# def first_occurence(nums: list[int], target: int) -> int:
#     left = 0
#     right = len(nums) -1
#     answer = -1

#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target: 
#             answer = mid
#             right = mid -1
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return answer

# user_input = input("Enter nums: ")
# numbers = [int(x) for x in user_input.split()]

# target = int(input("Enter your target: "))

# print(first_occurence(numbers, target))
