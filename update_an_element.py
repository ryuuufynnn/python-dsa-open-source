user_input = input("Enter number with spaces: ")

numbers = [int(x) for x in user_input.split()]

target = int(input("Enter a target number: "))

new_value = int(input("Enter a new value: "))

# for num in numbers:
#     if num == target:
#         numbers.remove(target)
#         numbers.append(new_value)
#         break
# print(numbers)

# approach 2 what would you choose prof?
for num in range(len(numbers)):
    if numbers[num] == target:
        numbers[num] = new_value
        break

print(numbers)