#if the number of arguments is unknown, add * before the parameter name in the function definition.
def add_nums(*nums):
    sum =0
    for num in nums:
        sum +=num
    return sum

print("Total: ",add_nums(2,5,6,7,8,13))