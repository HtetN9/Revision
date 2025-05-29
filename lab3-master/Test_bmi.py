import lab2.bmi as bmi

def test_bmi_normal_weight():
#    result = 0
    height = 1.73
    weight = 57
    result = bmi.calculate_bmi(height,weight) 
    
    assert(result == 0)
def test_bmi_over_weight():
#    result = 0
    height = 1.74
    weight = 83
    result = bmi.calculate_bmi(height,weight) 
    
    assert(result == 1)
def test_bmi_under_weight():
#    result = 0
    height = 1.9
    weight = 25
    result = bmi.calculate_bmi(height,weight) 
    
    assert(result == -1)



