# Problem: Determine whether a list of integers contains any duplicate values.
number = input("Enter a numbers with spaces: ")

numbers = [int(x) for x in number.split()]

has_duplicates = len(numbers)!= len(set(numbers))

if has_duplicates:
    print(f"Duplicates found! {numbers}")
else:
    print("No duplicates.")