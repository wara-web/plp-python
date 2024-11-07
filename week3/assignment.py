#declare the function

def calculate_discount(price,discount_percent):

    if discount_percent >=20:
        final_price = price -(price*discount_percent/100)
        return final_price
    
    else:
        return price #no discount applied.
#prompting the user to enter the price and discount
price = float(input("Enter the original price: "))
discount_percent = float(input("what is the percentage discount:  "))
#calling the function
final_price= calculate_discount(price,discount_percent)

#price of the commodity after discount
print(f"The final price is: ${final_price:.2f}")