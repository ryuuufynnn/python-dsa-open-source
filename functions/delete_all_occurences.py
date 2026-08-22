def delete_all_occurences(nums: list[int], target: int) -> list[int]: # ang function ay expected na mag-return ng list of integers.
    new_list = []
    for x in range(len(nums)):
        if nums[x] != target:
            new_list = new_list + [nums[x]]
    return new_list

user_input = input("Enter nums: ")
numbers = [int(x) for x in user_input.split()]

target = int(input("Enter your target: "))

print(delete_all_occurences(numbers, target))

# Gumawa ng function na tatanggap ng listahan ng numbers at isang target.

# Tanggalin lahat ng occurrences ng target sa list.

# Kung walang target, dapat manatiling unchanged ang list.

# Test Cases
# Numbers: 1 2 3 2 4 2 5
# Target: 2

# Expected: 1 3 4 5
# Numbers: 5 7 9 11
# Target: 3

# Expected: 5 7 9 11