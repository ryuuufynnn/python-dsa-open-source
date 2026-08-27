# Problem: Given a list of numbers, return a new list with duplicates removed while preserving original order.
user_input = input("Enter a set of numbers with spaces: ")

numbers = [int(x) for x in user_input.split()]

duplicate_numbers = []

# for num in numbers:
#     if num not in duplicate_numbers:
#         duplicate_numbers.append(num)
#         # duplicate_numbers += numbers[num]
# print(duplicate_numbers)

# for num in numbers:
#     if num not in numbers:
#         duplicate_numbers.append(num)
# print(duplicate_numbers)

# mas manual na approach
for num in numbers:
    found = False
    for check in duplicate_numbers:
        if num == check:
            found = True
            break
    if found == False:
        duplicate_numbers = duplicate_numbers + [num]

print(duplicate_numbers)
