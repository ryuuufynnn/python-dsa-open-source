user_input = input("Enter numbers with spaces: ")

numbers = [int(x) for x in user_input.split()]

greater_numbers = []

for num in numbers:
    if num > 5:
        greater_numbers.append(num)

print(f"Numbers greater than 5: {greater_numbers}")
