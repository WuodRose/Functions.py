
def calculate_discount(price, discount_percent):
    """
    calculates the final price after applying a discount. 
    The function should take the original price (price) 
    and the discount percentage (discount_percent) as parameters.
    
           note//  If the discount is 20% or higher, apply the discount;
                  otherwise, return the original price.
    
         Using the calculate_discount function,
         prompt the user to enter the original price of an item and the discount percentage. 
         Print the final price after applying the discount, or if no discount was applied,
         print the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Get user input for the original price and discount percentage
original_price = float(input("Enter the original price of the item: ksh."))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Print the final price
print(f"The final price after applying the discount is: ksh.{final_price:.2f}")
