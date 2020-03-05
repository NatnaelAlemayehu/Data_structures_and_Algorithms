def bubble(list_a):
    # SCan not apply comparision starting with last item of list (No item to right)
    indexing_length = len(list_a) - 1
    sorted = False  # Create variable of sorted and set it equal to false

    while not sorted:  # Repeat until sorted = True
        sorted = True  # Break the while loop whenever we have gone through all the values

        for i in range(0, indexing_length):  # For every value in the list
            # if value in list is greater than value directly to the right of it,
            if list_a[i] > list_a[i+1]:
                sorted = False  # These values are unsorted
                list_a[i], list_a[i+1] = list_a[i +
                                                1], list_a[i]  # Switch these values
    return list_a  # Return our list "unsorted_list" which is not sorted.


print(bubble([4, 8, 1, 14, 8, 2, 9, 5, 7, 6, 6]))
