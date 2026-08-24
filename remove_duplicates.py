user_input = input("Enter a set of numbers with spaces: ")

numbers = [int(x) for x in user_input.split()]

duplicate_numbers = []

# for num in numbers:
#     if num not in duplicate_numbers:
#         duplicate_numbers.append(num)
#         # duplicate_numbers += numbers[num]
# print(duplicate_numbers)

for num in numbers:
    if num not in numbers:
        duplicate_numbers.append(num)
print(duplicate_numbers)