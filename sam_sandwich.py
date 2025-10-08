import math, datetime, phonenumbers
def force_number(number_type = 0,lower_boundary = 0,upper_boundary = 10,number_action_type = None,rounding_digits = 0):
    internal_number_types = (int,float)
    number_action_types = (None,math.floor,math.ceil)
    external_number_types = ("integer","decimal number")
    while True:
        try:
            number = internal_number_types[number_type](input(f"Enter a valid {external_number_types[number_type]}:"))
        except ValueError:
            print(f"Invalid value. Enter a valid {external_number_types[number_type]}.")
            continue
        if  lower_boundary <= number <= upper_boundary:
            if number_action_type is not None and number_type == 1:
                if number_action_type == 0:
                    number = round(number,rounding_digits)
                else: 
                    number = number_action_types[number_action_type](number)
            return number
        else:
            print(f"Unexpected value. Enter a valid {external_number_types[number_type]} between {lower_boundary} and {upper_boundary}.")

def force_name(string_type = 0,upper = 20,lower = 2):
    while True:
        string_types = ["first", "middle", "last"]
        string = str(input(f"What is your {string_types[string_type]} name?"))
        string = string.replace(" ","").lower().capitalize()
        if string.isalpha() and len(string) >= lower and len(string) <= upper :
            return string
            #Returns valid string
        elif not string.isalpha() and string != "":
            print("Error: Invalid string\nExpected only alphabetic characters")
        elif len(string) < lower or len(string) > upper:
            print(f"Error: Unexpected value\nExpected a string between {lower} and {upper} characters.")

def bread_selection(): #allows user to select their preferred bread
    bread_list = ["White", "Brown", "Italian", "Granary"]
    count=0
    print("We have the following breads: ")
    while count < len(bread_list): #prints out each item on the list
        print(count+1," ", bread_list [count])
        count += 1
    print("Which bread do you want?")
    bread_selected = force_number(0,1,4)-1
    print(f"You have selected {bread_list[bread_selected]}.")
    return bread_list[bread_selected] #returns back a string

def meat_selection():
    meat_list = ["Chicken", "Beef", "Pork", "Lamb"]
    count=0
    print("We have the following meats: ")
    while count < len(meat_list): #prints out each item on the list
        print(count+1," ", meat_list[count])
        count += 1
    print("Which meat do you want?")
    meat_selected = force_number(0,1,4)-1
    print(f"You have selected {meat_list[meat_selected]}.")
    return meat_list[meat_selected]

def salad_selection():
    salad_list = ["Lettuce","Tomato","Carrot","Cucumber","Onions"]
    count=0
    print("We have the following salads: ")
    while count < len(salad_list): #prints out each item on the list
        print(count+1," ", salad_list[count])
        count += 1
    print("Which salad do you want?")
    salad_selected = force_number(0,1,5)-1
    print(f"You have selected {salad_list[salad_selected]}.")
    return salad_list[salad_selected]

def dressing_selection():
    dressing_list = ["Ranch Dressing","Caeser Dressing","Blue Cheese Dressing","Thousand Island Dressing"]
    count=0
    print("We have the following dressings: ")
    while count < len(dressing_list): #prints out each item on the list
        print(count+1," ", dressing_list[count])
        count += 1
    print("Which dressing do you want?")
    dressing_selected = force_number(0,1,4)-1
    print(f"You have selected {dressing_list[dressing_selected]}.")
    return dressing_list[dressing_selected]

def cheese_selection():
    cheese_list = ["Cheddar cheese","Swiss cheese","Gouda Cheese","Brie Cheese","Monterey Jack Cheese","Blue Cheese"]
    count=0
    print("We have the following cheeses: ")
    while count < len(cheese_list): #prints out each item on the list
        print(count+1," ", cheese_list[count])
        count += 1
    print("Which cheese do you want?")
    cheese_selected = force_number(0,1,6)-1
    print(f"You have selected {cheese_list[cheese_selected]}")
    return cheese_list[cheese_selected]

#main program
def main():
    sandwich_order = []
    print("Welcome to Sam's Sandwhich Shop")
    bread_choice = bread_selection() #creating a variable that calls up the bread function and returns their choice print(f"Your selected bread: {bread_choice}")
    meat_choice = meat_selection()
    salad_choice = salad_selection()
    dressing_choice = dressing_selection()
    cheese_choice = cheese_selection()
    name = force_name() + " " + force_name(2)
    cellphone_number = input("What is your phone number?")
    #while True:
        #try:
            #cellphone_number = int(input("What is your phone number?"))
        #except:
            #print("Invalid phone number")
        #if cellphone_number(phonenumbers.is_valid_number) == True:
            #break
        #else:
            #print("Invalid phone number")
    time = datetime.datetime.now()
    sandwich_order.append(f"******** Order for {name} {cellphone_number} ********")
    sandwich_order.append(f"\nName: {name}")
    sandwich_order.append(f"\nCellphone number: {cellphone_number}")
    sandwich_order.append(f"\nDate/time: {time}")
    sandwich_order.append(f"\nBread: {bread_choice}")
    sandwich_order.append(f"\nMeat: {meat_choice}")
    sandwich_order.append(f"\nSalad: {salad_choice}")
    sandwich_order.append(f"\n******** End of Order: {time} ********")
    outf = open("order_record.txt","a")
    for i in sandwich_order:
        outf.write(i)
    outf.write("\n\n")
    outf.close()
    
main()