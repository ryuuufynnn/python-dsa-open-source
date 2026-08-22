user_input = input("Enter numbers with spaces: ")

numbers = [int(x) for x in user_input.split()]

target = int(input("Enter all target numbers: "))

for num in range(len(numbers) -1, -1, -1):
    if numbers[num] == target:
        numbers.pop(num) # pop() need's an index; remove() needs a value
print(numbers)


# delete lahat ng magkakaparehas