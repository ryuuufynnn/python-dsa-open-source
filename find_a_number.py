# Problem: Determine whether a target number appears in a list of integers.
user_input = input("Enter numbers with spaces: ")

numbers = [int(x) for x in user_input.split()]

target = int(input("Enter number to find: "))

found = False

for num in numbers:
    if num == target:
        found = True # set the found = True if the target is found
        break # stop na ang loop pag True na ang found.
if found: # pwedeng (if found) na lang
    print(f"Number {target} found!")
else:
    print("Number not found.")