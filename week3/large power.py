def large_power(base, exponent):

    #calculate the result of base raised to power exponent

    result = base ** exponent
    #is the result greater than 5000?
    if result>5000:
        return True

    else:
        return False

#example of base and exponents..
print(large_power(3,5))