user_input = input("Enter a number with spaces: ")

numbers = [int(x) for x in user_input.split()]

target = int(input("Enter a target number: "))

found = -1 # not found
count = 0 # count 0 muna

for num in range(len(numbers)): # traverse the list using indexes 
    if numbers[num] == target:
        count += 1 # increase occurence count
        if count == 1: # if this is the first occurence count
            found = num # found - save the current index

if found == -1: # if the target is not found
    print(f"Number {target} not found")
else: 
    print(f"Number {target} found in an index {found}")
    print(f"Number {target} appears {count}x")
