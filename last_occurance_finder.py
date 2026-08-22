user_input = input("Enter numbers with spaces: ")

numbers = [int(x) for x in user_input.split()]

target = int(input("Enter the target number: "))

index = 0 # last

for last in range(len(numbers) -1, -1, -1):
    if numbers[last] == target:
        index = last
        break # break if the last occurence found.

if index != -1:
    print(f"Last occurence of {target} is at index {index}")
else:
    print(f"Number {target} not found.")