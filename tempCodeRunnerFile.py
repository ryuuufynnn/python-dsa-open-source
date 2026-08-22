# Gumawa ng program na tatanggap ng listahan ng numbers at isang target number.

# Hanapin ang first number na strictly greater than the target, at i-report ang value at index nito.

user_input = input("Enter a numbers: ")

numbers = [int(x) for x in user_input.split()]

target = int(input("Enter a target number: "))

first = numbers[0]
index = -1
target_greater_than_first = False

for x in numbers: # wala ako idea kung paano gagawin sa range and len kaya simple approach muna ginawa ko;
    if x > target:
        target = x
        break
for x in range(len(numbers) -1, -1, -1):
    if numbers[x] == target:
        index = x


print(f"Value: {target}")
print(f"Index: {index}")

        

