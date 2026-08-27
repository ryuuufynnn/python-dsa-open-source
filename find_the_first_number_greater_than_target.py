# Problem: Given a list of numbers and a target, find the first value greater than the target and its index.
# Gumawa ng program na tatanggap ng listahan ng numbers at isang target number.

# Hanapin ang first number na strictly greater than the target, at i-report ang value at index nito.

user_input = input("Enter a numbers: ")

numbers = [int(x) for x in user_input.split()]

target = int(input("Enter a target number: "))

index = -1
found = -1
count = 0

for x in numbers: # wala ako idea kung paano gagawin sa range and len kaya simple approach muna ginawa ko;
    if x > target:
        found = x
        index = count
        break
    count += 1
# for x in range(len(numbers~) -1, -1, -1):
#     if numbers[x] == target:
#         index = count # tama rin ito at gumagana, pero baka maarte si sir, joke ahah


print(f"Value: {found}")
print(f"Index: {index}")

        

