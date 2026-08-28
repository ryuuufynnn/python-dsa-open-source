# from [5, 4, 3, 2, 1] to [1, 2, 3, 4, 5] - aayusin ang list of numbers in ascending order;

def bubble_sort(array: list[int]) -> list[int]:
    is_swap = True
    right = len(array) -1

    while is_swap:
        is_swap = False
        for i in range(right):
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
                is_swap = True
    return array
print(bubble_sort([4,8,10,1]))