
def calculate_price(expenses):
    """
    Calculate the price after applying a discount based on the expenses.

    Args:
        expenses (float): The total expenses.

    Returns:
        None
    """
    if expenses > 100:
        if expenses > 200:
            discount = 20  # Apply a discount of 20 if expenses are greater than 200
        else:
            discount = 10  # Apply a discount of 10 if expenses are between 100 and 200
    else:
        discount = 0  # No discount if expenses are less than or equal to 100
    
    price = round(expenses - discount, 2)  # Round the price to 2 decimal places
    print(f"John's expenses: ${expenses}")
    print(f"Discount applied: ${discount}")
    print(f"Price after discount: ${price}")

# Example usage
john_expenses = 210.23
calculate_price(john_expenses)