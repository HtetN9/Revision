import employee_info

def test_get_employees_by_age_range():
    upper_limit = 31
    lower_limit = 17
    expected_names = ['John','Jane','Mary']
    return_list = employee_info.get_employees_by_age_range(lower_limit,upper_limit)
    for i in return_list:
        for k in expected_names:
            if i['name'] == k:
                expected_names.remove(k)
    
    assert(expected_names == [])

def test_calculate_average_salary():

    excepted_salary = 60166.67
    returned_value = employee_info.calculate_average_salary()

    assert(excepted_salary == returned_value)


def test_get_employees_by_dept():
    department = "Marketing"
    expected_names = ["Jane","Mary"]
    return_name_list = employee_info.get_employees_by_dept(department)
    for i in return_name_list:
        for l in expected_names:
            if i["name"] == l:
                expected_names.remove(l)

    assert(expected_names == [])

    

