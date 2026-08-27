# Problem: Find the largest and the second largest numbers in a list of integers.
# user_input = input("Enter numbers with spaces: ")

# numbers = [int(x) for x in user_input.split()]

# largest = numbers[0]
# second_largest = numbers[0] 
# print(second_largest) # debug

# for num in numbers:
#     if num > largest:
#         second_largest = largest # update both if num is greater than to largest
#         largest = num # update to largest

#     elif num > second_largest and num != largest: 
#         second_largest = num

# print(f"first largest {largest}")
# print(f"second {second_largest}")

# if largest or first and second largest ang hinahanap, no need na gumamit ng len;

def largest_and_second_largest(nums: list[int]) -> int:

    largest = nums[0]
    second = nums[0]

    for x in nums:
        if x > largest:
            second = largest
            largest = x
        if x < second and x != largest:
            second = x
    # return largest, second
    return f"largest: {largest}\nsecond: {second}"
print(largest_and_second_largest([1, 5, 6, 3]))

# function approach

# problem: find the largest and the second largest number in a list of numbers.