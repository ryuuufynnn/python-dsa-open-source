# Problem: Find a target in a sorted list or determine the index where it should be inserted.
user_input = input("n: ")
nums = [int(x) for x in user_input.split()]

target = int(input("t: "))

index_left = 0
index_right = len(nums) -1
found = False
answer = -1 # not found

while index_left <= index_right:
    mid = (index_left + index_right) // 2

    if nums[mid] == target:
        answer = mid
        found = True
        break
    elif nums[mid] < target:
        index_left = mid + 1
    else:
        index_right = mid - 1

if found:
    print(answer)
else:
    answer = index_left
    print(f"left {answer}")

    


            
        
# serach left lang ang hahanapin sa left magsisimula sa approach na to