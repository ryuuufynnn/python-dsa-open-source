
user_input = input("Enter numbers with spaces: ")

numbers = [int(x) for x in user_input.split()]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
print(f"Smallest number: {smallest}")