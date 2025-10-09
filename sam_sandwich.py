import math, datetime, phonenumbers

# Function to force the user to input a number within a specified range and apply certain actions like rounding
def force_number(number_type = 0, lower_boundary = 0, upper_boundary = 10, number_action_type = None, rounding_digits = 0):
    # Internal types for validation
    internal_number_types = (int, float)
    number_action_types = (None, math.floor, math.ceil)  # Valid actions (None, floor, ceil)
    external_number_types = ("integer", "decimal number")  # Human-readable types for error messages

    while True:
        try:
            # Try to convert input to the requested number type (integer or float)
            number = internal_number_types[number_type](input(f"Enter a valid {external_number_types[number_type]}:"))
        except ValueError:
            print(f"Invalid value. Enter a valid {external_number_types[number_type]}.")
            continue  # Repeat the loop if input is invalid

        # Check if the number is within the specified boundaries
        if lower_boundary <= number <= upper_boundary:
            if number_action_type is not None and number_type == 1:  # Only applies number actions to decimals
                if number_action_type == 0:  # Round if action type is 0
                    number = round(number, rounding_digits)
                else:
                    number = number_action_types[number_action_type](number)  # Apply floor or ceil
            return number  # Return the validated and possibly modified number
        else:
            print(f"Unexpected value. Enter a valid {external_number_types[number_type]} between {lower_boundary} and {upper_boundary}.")

# Function to force user to input a valid name (first, middle, or last)
def force_name(string_type = 0, upper = 20, lower = 2):
    while True:
        string_types = ["first", "middle", "last"]  # Different types of names
        string = str(input(f"What is your {string_types[string_type]} name?"))
        string = string.replace(" ","").lower().capitalize()  # Clean up input: remove spaces, lowercase, capitalize

        # Check if the name is alphabetic and within the length limits
        if string.isalpha() and len(string) >= lower and len(string) <= upper:
            return string  # Return valid name
        elif not string.isalpha() and string != "":
            print("Error: Invalid string\nExpected only alphabetic characters")
        elif len(string) < lower or len(string) > upper:
            print(f"Error: Unexpected value\nExpected a string between {lower} and {upper} characters.")

# Function to allow the user to select a type of bread from a list
def bread_selection():
    bread_list = ["White", "Brown", "Italian", "Granary"]
    count = 0
    print("We have the following breads: ")
    
    # Display bread options
    while count < len(bread_list):
        print(count + 1, " ", bread_list[count])
        count += 1
    
    print("Which bread do you want?")
    # Get valid bread choice using force_number function (choices between 1 and 4)
    bread_selected = force_number(0, 1, 4) - 1
    print(f"You have selected {bread_list[bread_selected]}.")
    return bread_list[bread_selected]  # Return the selected bread

# Function for meat selection
def meat_selection():
    meat_list = ["Chicken", "Beef", "Pork", "Lamb"]
    count = 0
    print("We have the following meats: ")
    
    # Display meat options
    while count < len(meat_list):
        print(count + 1, " ", meat_list[count])
        count += 1
    
    print("Which meat do you want?")
    # Get valid meat choice
    meat_selected = force_number(0, 1, 4) - 1
    print(f"You have selected {meat_list[meat_selected]}.")
    return meat_list[meat_selected]  # Return selected meat

# Function for salad selection
def salad_selection():
    salad_list = ["Lettuce", "Tomato", "Carrot", "Cucumber", "Onions"]
    count = 0
    print("We have the following salads: ")
    
    # Display salad options
    while count < len(salad_list):
        print(count + 1, " ", salad_list[count])
        count += 1
    
    print("Which salad do you want?")
    # Get valid salad choice
    salad_selected = force_number(0, 1, 5) - 1
    print(f"You have selected {salad_list[salad_selected]}.")
    return salad_list[salad_selected]  # Return selected salad

# Function for dressing selection
def dressing_selection():
    dressing_list = ["Ranch Dressing", "Caeser Dressing", "Blue Cheese Dressing", "Thousand Island Dressing"]
    count = 0
    print("We have the following dressings: ")
    
    # Display dressing options
    while count < len(dressing_list):
        print(count + 1, " ", dressing_list[count])
        count += 1
    
    print("Which dressing do you want?")
    # Get valid dressing choice
    dressing_selected = force_number(0, 1, 4) - 1
    print(f"You have selected {dressing_list[dressing_selected]}.")
    return dressing_list[dressing_selected]  # Return selected dressing

# Function for cheese selection
def cheese_selection():
    cheese_list = ["Cheddar cheese", "Swiss cheese", "Gouda Cheese", "Brie Cheese", "Monterey Jack Cheese", "Blue Cheese"]
    count = 0
    print("We have the following cheeses: ")
    
    # Display cheese options
    while count < len(cheese_list):
        print(count + 1, " ", cheese_list[count])
        count += 1
    
    print("Which cheese do you want?")
    # Get valid cheese choice
    cheese_selected = force_number(0, 1, 6) - 1
    print(f"You have selected {cheese_list[cheese_selected]}")
    return cheese_list[cheese_selected]  # Return selected cheese

# Function to get a valid cellphone number with phone number validation
def get_cellphone_number():
    while True:
        raw_number = "+64" + input("Enter your phone number: ")  # Adding country code
        try:
            parsed_number = phonenumbers.parse(raw_number)  # Parse phone number
        except exception:
            print("Error:\nEnter a valid phone number")
            continue  # Restart loop on exception

        if phonenumbers.is_valid_number(parsed_number):  # Check if phone number is valid
            return raw_number
        else:
            print("Error:\nEnter a current phone number")  # If invalid, prompt again

def record_order():
    # Write order details to a file
    outf = open("order_record.txt", "a")
    for i in sandwich_order:
        outf.write(i)
    outf.write("\n\n")
    outf.close()

# Main program
def main():
    sandwich_order = []  # List to store sandwich order details
    print("Welcome to Sam's Sandwich Shop")

    # Collect user inputs for different sandwich components
    bread_choice = bread_selection()
    meat_choice = meat_selection()
    salad_choice = salad_selection()
    dressing_choice = dressing_selection()
    cheese_choice = cheese_selection()

    # Collect user's name (first and last)
    name = force_name() + " " + force_name(2)

    # Get user's cellphone number
    cellphone_number = get_cellphone_number()

    # Get current date and time for the order
    time = datetime.datetime.now()

    # Add order details to the sandwich_order list
    sandwich_order.append(f"******** Order for {name} {cellphone_number} ********")
    sandwich_order.append(f"\nName: {name}")
    sandwich_order.append(f"\nCellphone number: {cellphone_number}")
    sandwich_order.append(f"\nDate/time: {time}")
    sandwich_order.append(f"\nBread: {bread_choice}")
    sandwich_order.append(f"\nMeat: {meat_choice}")
    sandwich_order.append(f"\nSalad: {salad_choice}")
    sandwich_order.append(f"\n******** End of Order: {time} ********")

    # Write order details to a file
    record_order()

# Run the main function to start the program
main()
