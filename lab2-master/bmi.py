def calculate_bmi(height,weight):
    #Prints out the height and weight beforehand
    print("Height = " + str(weight))
    print("Weight = " +  str(height))
    # Calculates BMI and displays it
    bmi = weight / (height * height)
    print("Body Mass Index (BMI): ", round(bmi,2))

    # Determines the user's weight classification 
    if bmi < 18.5:
        weight_class = "Under Weight"
        return_value = -1
    elif bmi <= 25.0:
        weight_class = "Normal Weight"
        return_value = 0
    else:
        weight_class = "Over Weight"
        return_value = 1
    print("The user is", weight_class)

    return return_value


calculate_bmi(height=1.73,weight=57)