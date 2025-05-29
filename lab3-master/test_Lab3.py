import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

# Checks if the function returns value 1 if >= 10 numbers are entered
# REQ-03
def test_bubble_sort_is_input_greater_than_ten():
    result = []
    input_arr = [69,420,12,66,11,90,3,34,78,102,48]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == 1)

# Checks whether it returns 0 when there's no numbers entered
# REQ-04
def test_bubble_sort_no_number_entered():
    result = []
    input_arr = []

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert (result == 0)
    
# Checks if it returns 2 if the values are not int
# REQ-05
def test_bubble_sort_input_not_int():
    result = []
    input_arr = [69,'alpha',12,66.95959,'m','MOO',48,'meow']

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == 2)