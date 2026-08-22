user_input = input("Enter an even and odd numbers: ") # user_input

numbers = [int(x) for x in user_input.split()] # convert into int

positive_count = 0 
negative_count = 0 
zero_count = 0

for num in numbers: # loop the user_input
    if num >= 1:
        positive_count += 1
    elif num == 0:
        zero_count += 1
    else:
        negative_count += 1

print(f"Positive: {positive_count}") # print the total of even numbers
print(f"Negative: {negative_count}")
print(f"Zero: {zero_count}")