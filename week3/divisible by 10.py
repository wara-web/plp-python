#declare the function

def divisible_by_10(num):
    #check if the number is divisible by 10
    if num % 10 == 0:
        return True
    else:
        return False
    
#example

print(divisible_by_10(20))