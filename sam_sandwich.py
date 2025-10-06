
def bread_selection(): #allows user to select their preferred bread
    bread_list = ["White", "Brown", "Italian", "Granary"]
    count=0
    print("We have the following breads: ")
    while count < len(bread_list): #prints out each item on the list
        print(count+1," ", bread_list [count])
        count += 1
    bread_selected=int(input("Which bread did you want? Enter a number"))
    return bread_list [bread_selected] #returns back a string

def meats_selection():
    meats_list = ["White", "Brown", "Italian", "Granary"]
    count=0
    print("We have the following breads: ")
    while count < len(bread_list): #prints out each item on the list
        print(count+1," ", bread_list [count])
        count += 1
    bread_selected=int(input("Which bread did you want? Enter a number"))
#main program
def main():
    print("Welcome to Sam's Sandwhich Shop")
    bread_choice = bread_selection() #creating a variable that calls up the bread function and returns their choice print(f"Your selected bread: {bread_choice}")
    meat_choice = meats_selection()

main()