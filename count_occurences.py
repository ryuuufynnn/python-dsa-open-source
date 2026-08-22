user_input = input("Enter numbers with spaces: ")

numbers = [int(x) for x in user_input.split()]

target = int(input("Enter number to count: "))

count = 0

for num in numbers:
    if num == target:
        count += 1

print(f"Number {target} appears {count} times.")