def tempconvert(type,temp):
    if type == "f":
        result = [(temp-32)*5/9, "Fahrenheit", "Celsius"]
    else:
        result = [(temp * 9/5) + 32, "Celsius", "Fahrenheit"]
    return result
