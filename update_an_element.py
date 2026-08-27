# user_input = input("Enter number with spaces: ")

# numbers = [int(x) for x in user_input.split()]

# target = int(input("Enter a target number: "))

# new_value = int(input("Enter a new value: "))

# for num in numbers:
#     if num == target:
#         numbers.remove(target)
#         numbers.append(new_value)
#         break
# print(numbers)

# approach 2 what would you choose prof?
# for num in numbers:
#     if numbers[num] == target:
#         numbers[num] = new_value
#         break

# print(numbers)

def update_element(nums: list[int], target: int, new_value: int) -> int:
    for num in nums:
        if nums[num] == target:
            nums[num] = new_value
            break # if isa lang ang number na gustong i update:
            # input: 1 2 3 2 2
            # target: 2
            # output: 1 4 3 2 2
    return nums

print(update_element([1, 2, 3, 2, 2], 2, 4))