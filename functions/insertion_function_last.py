def insertion_function_last(array: list[int], new_data: int) -> list[int]:

    length = 0
    for _ in array: # manual for len()
        length += 1

    result = [0] * (length + 1)

    for x in range(length):
        result[x] = array[x]
    result[length] = new_data
    
    return result


print(insertion_function_last([1, 2, 3,4 , 5], 90))

# output: [1, 2, 3, 4, 5, 90]