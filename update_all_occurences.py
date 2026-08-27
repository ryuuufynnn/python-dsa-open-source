# Problem: Replace every occurrence of a target number in a list with a new value.
user_input = input("Enter number with spaces: ")

numbers = [int(x) for x in user_input.split()]

target = int(input("Enter a number to update: "))
new_value = int(input("Enter a new value: "))

for num in range(len(numbers) -1, -1, -1):
    if numbers[num] == target:
        numbers[num] = new_value
print(numbers)