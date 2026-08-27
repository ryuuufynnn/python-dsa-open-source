# Problem: Given a list of numbers and a threshold, return a list of numbers greater than the threshold.
# user_input = input("Enter numbers with spaces: ")

# numbers = [int(x) for x in user_input.split()]

# greater_numbers = []

# for num in numbers:
#     if num > 5:
#         greater_numbers.append(num)

# print(f"Numbers greater than 5: {greater_numbers}")

def build_a_new_list(nums: list[int], greater_than: int) -> int:
    greater_numbers = []

    for num in nums:
        if num > greater_than:
            greater_numbers += [num] # or grater_numbers.append(num)
    return greater_numbers

nums = [1, 2, 5, 9, 8, 7]
five = 5
print(build_a_new_list(nums, five))