print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # Copy input list to result list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

    # Checks each items of the array to check if it's int or not; if it isn't, ends the function
    for i in arr_result:
        if type(i) != int:
            arr_result = 2
            return 2

    if n < 10 and n != 0: # <-- To make sure if the array's length is less than 10 and not empty
        # Traverses through all array elements
        for i in range(n - 1):
            # range(n) also work but outer loop will
            # repeat one time more than needed.

            # Last i elements are already in place
            for j in range(0, n - i - 1):
            
                if sorting_order == SORT_ASCENDING:
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]


                elif sorting_order == SORT_DESCENDING:
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
                
                else:
                    # <-- Return an empty array if the sorting_order isn't either 0/1 (Ascending and desc.)
                    arr_result = []

    elif n == 0: # <-- Returns 0 if the array is empty
        arr_result = 0
    else: # <-- Retruns 1 if it's >= 10 numbers 
        arr_result = 1

    return arr_result

def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)

if __name__ == "__main__":
    main()


