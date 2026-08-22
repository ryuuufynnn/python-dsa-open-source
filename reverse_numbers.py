user_input = input("Enter numbers to reverse: ")

numbers = [int(x) for x in user_input.split()]

reversed_numbers = []

for num in range(len(numbers) -1, -1, -1):
    reversed_numbers.append(numbers[num])
print(reversed_numbers)