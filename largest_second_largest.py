
user_input = input("Enter numbers with spaces: ")

numbers = [int(x) for x in user_input.split()]

largest = numbers[0]
second_largest = 0 # -10 -20 -30 may bug

print(second_largest) # debug

for num in numbers:
    if num > largest:
        second_largest = largest # update both if num is greater than to largest
        largest = num # update to largest

    elif num > second_largest and num != largest: 
        second_largest = num

print(f"first largest {largest}")
print(f"second {second_largest}")

# if largest or first and second largest ang hinahanap, no need na gumamit ng len;