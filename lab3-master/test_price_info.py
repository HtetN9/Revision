import price_info

def test_total_cost_shipping():
    cost = 46.75
    returned_result = price_info.total_cost_shopping()
    assert(cost == returned_result)

def test_cost_of_fruit():
    fruit = "apple"
    quantity = 10
    returned_value = price_info.cost_of_fruits(fruit,quantity)

    assert(returned_value == 12)

test_cost_of_fruit()
