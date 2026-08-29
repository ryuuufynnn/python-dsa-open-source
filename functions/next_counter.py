# auto add to the last count of the list 
# input: [1, 2, 3, 4, 5]
# output: [1, 2, 3, 4, 5, 6]

def counter(array: list[int]) -> list[int]:

    length = 0
    for _ in array:
        length += 1
    result = [0] * (length + 1)

    for x in range(length):
        result[x] = array[x]
    result[length] = length + 1
    return result

print(counter([1, 2, 3, 4]))