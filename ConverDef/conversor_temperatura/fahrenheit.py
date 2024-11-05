# Fahrenheit a Celsius
def conversor_f_c(f):
    result = (f - 32) / 1.8
    return result


# Fahrenheit a Kelvin
def conversor_f_k(f):
    result = ((f - 32) / 1.8) + 273.15
    return result
