def bubble_sort(array):
    n = len(array)
    while True:
        swapped = False
        for i in range(n - 1):
            if array[i] < array[i + 1]:
                # Swap the elements
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        # If no swaps were made, the array is sorted
        if not swapped:
            break
    return array

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = bubble_sort(numbers)
print("Sorted array:", sorted_numbers)




