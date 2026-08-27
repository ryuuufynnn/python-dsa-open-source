# Problem: Given a list of numbers and a target, remove occurrences of the target from the list.
user_input = input("Enter a number with spaces: ")

numbers = [int(x) for x in user_input.split()]

target_deletion = int(input("Enter a number to delete: "))

for num in numbers:
    if num == target_deletion:
        numbers.remove(target_deletion)
        break
    else:
        # deleted_numbers.append(num) # tama rin ito e, pero bakit?
        numbers
print(numbers)