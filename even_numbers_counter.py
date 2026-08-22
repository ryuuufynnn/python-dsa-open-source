user_input = input("Enter an even and odd numbers: ") # user_input

numbers = [int(x) for x in user_input.split()] # convert into int

even_count = 0 # even number counter

for num in numbers: # loop the user_input
    if num % 2 == 0: # check if the number is even
        even_count += 1

print(f"There are {even_count} even numbers.") # print the total of even numbers