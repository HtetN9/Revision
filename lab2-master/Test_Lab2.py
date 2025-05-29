import lab2

def test_find_min_max(): # Test for the fn find_min_max()
    min_max = []
    list_to_feed = [69,33,2323,340,2,1000,354,5]
    min_max = lab2.find_min_max(list_to_feed)
    print(min_max)
    print(min_max[0],min_max[1])
    
    assert (min_max[0] == 2 and min_max[1] == 2323)

def test_calc_average(): # Test for the fn calc_average()
    list_to_feed = [1,7,3,66,7,34,2]
    expected_value = 120
    value_returned = lab2.calc_average(list_to_feed)

    assert(expected_value == value_returned)


def test_calc_median_temperature(): # Test for the fn calc_median_temp()
    list_to_feed = [2,5,6,7,10]
    expected_value = 6
    value_returned = lab2.calc_median_temperature(list_to_feed)

    assert(expected_value == value_returned)