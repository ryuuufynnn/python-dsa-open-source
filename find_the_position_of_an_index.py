# Problem: Find the first index of a target number in a list, or report that it is absent.
user_input = input("Enter a number with spaces: ")

numbers = [int(x) for x in user_input.split()]

target = int(input("Enter the target number: "))

found = -1 # not found value

for num in range(len(numbers)):
    if numbers[num] == target:
        found = num
        break
if found != -1:
    print(f"Number {target} found in index {found}")
else:
    print(f"Number {target} not found")
