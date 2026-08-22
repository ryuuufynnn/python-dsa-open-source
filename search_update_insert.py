user_input = input("Enter number with spaces: ")

numbers = [int(x) for x in user_input.split()]

print("Choose an operation:")
print("1. Search")
print("2. Update")
print("3. Insert")

operator = int(input("Enter choice: "))
if operator == 1:
    target = int(input("Enter a target: "))
    found = False
    for num in numbers:
        if num == target:
            found = True
            break # if nahanap na
    print(f"Target {target} found")

if operator == 2:
    target = int(input("Enter a target: "))
    new_value = int(input("Enter a new value: "))
    for num in range(len(numbers) -1, -1, -1):
        if numbers[num] == target:
            numbers[num] = new_value
    print(numbers)

# if operator == 3:
#     new_number = int(input("Enter a new list value: "))
#     index_position = int(input("Enter an index position: "))
#     numbers.insert(index_position, new_number) # insert(index, value)

# approach 2 for insertion;
if operator == 3:
    new_number = int(input("Enter a new list value: "))
    index_position = int(input("Enter an index position: "))

    new_list = [] # create a new empty list muna
    for num in range(index_position): # add lahat ng numbers before the index
        new_list.append(numbers[num])
    new_list.append(new_number)

    for num in range(index_position, len(numbers)): # add new number # add all numbers after the index
        new_list.append(numbers[num])

    numbers = new_list # replace the old list with a new one

    print(numbers) # print the new list of numbers
