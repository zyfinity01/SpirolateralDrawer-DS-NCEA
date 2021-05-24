import sys  # imports sys for the sys.exit() function that allows the program to be stopped
import turtle  # imports turtle module
wn = turtle.Screen()  # create a screen
turtle.setup(800, 720)  # setup screen with H x W dimentions
turtle = turtle.Turtle()  # creates turtle
x = "-----"  # empy line to seperate different parts in the program to be more aesthetically pleasing used in a variable to be easy to use anywhere in the code

fav = []


def display_menu():  # display menu shows different options to select from a list
    global items  # globalised items to make items list accessible in the whole code
    items = ["Display stored spirolateral",
             "Add a new spirolateral to the list",
             "Draw a spirolateral from number",
             "Delete a spirolateral from the list",
             "Quit the program"]  # List is being used to make it easier to read and easier to add extra items if necesarry later down the line
    num = 1
    for item in items:  # makes list start from 1 instead of 0
        print(num, item)  # prints number next to item in list.
        num = num + 1


def get_int(lower_lim, upper_lim, prompt):  # This function checks for input validity and can be called anywhere in the code
    choice = -1
    while choice == -1:
        try:
            choice = int(input(prompt))
            if choice < lower_lim or choice > upper_lim:
                print("Out of range!")
                choice = -1
        except:
            print("Not a valid integer")
    return choice


def display_fav():  # displays the favourite list for stored spirolaterals
    print(10*x)  # prints lines to make the program look cleaner
    global fav, spirolateral
    num = 1
    if len(fav) > 0:
        for Spirolateralname in fav:  # prints list of spirolaterals and places a number next to it counting from 1
            print(num, Spirolateralname)
            num = num + 1
    else:
        # This prints that the list is empty if the length of the list fav is less than 0 (nothing)
        print("sorry the favourites list is empty")
        main()  # Calls on the "main" function so it can display the menu choices


def find_digitalroot(n):
    return (n - 1) % 9 + 1 if n else 0  # This function is the function for digital root


def multiplication(n):
    run = 1
    while True:
        # yield is used instead of return as it can produce a sequence of values
        yield find_digitalroot(n*run)
        run += 1


def draw_spiro():  # This function draws spirolaterals
    turtle.reset()  # This resets the turtle canvas everytime the function is run to clear any previously drawn spirolaterals
    # asks for an input for what the digital root number is
    timetableinput = int(input("What timetable do you want to draw a digital root from 2-20? "))
    # asks for the angle the turtle will go left
    angle = int(input("What angle do you want (30 - 120) recommended? "))
    # asks for the speed of the drawing
    speed_ = int(input("How fast do you want to draw the spirolateral, Slow to fast : 1 - 10 "))
    # the size/radius of the spirolateral
    spirosize = int(input("How big do you want the spirolateral to be? 10 - 20 recommended "))
    # prints the digital root number (AKA distance)
    printdistance = input(
        "Do you want to print the digital root as the spirolateral is being drawn? yes or no? ").lower()
    # creates a digital root of the original number for the drawing stopper to know the starting point where it has to stop
    originalspiro_cor = find_digitalroot(timetableinput)
    loop = 0  # setting up loop variable to 0, variable "loop" calculates how many times the loop has been run
    digitrootnum = 0
    # The Variable "Addone" is the number that gets times by with the user times table "timetableinput" input.
    Addone = 1
    while True:  # loop calculates the distance the spirolateral is going forwards
        digitrootnum = timetableinput * Addone
        # multiplies the digital root and digitrootnum input
        spirodistance = find_digitalroot(digitrootnum)
        turtle.speed(speed_)
        Addone = Addone + 1  # Add one gets 1 added everytime the loop runs, this is because the "timetableinput" input is times by a number
        turtle.forward(spirodistance * spirosize)  # times 10 to increase size
        # takes a variety of inputs that relate to the word yes
        if printdistance in ['yes', 'y', 'yea', 'sure', 'ok']:
            print(spirodistance)  # prints the distance
        turtle.left(angle)  # turns depending on the angle inputted
        n = turtle.position()  # graps x,y coordinates for turtles position
        loop = loop + 1  # adds 1 to the loop so on next playback the loop will be 2 and then stop the spirolateral when it finishes
        # breaks the loop when the conditions of the current turtle position and original start turtle-
        # position are under 0.01 (so if they are the same) and then also checks if restarts = 2 or more to ensure it doesnt break when the loop first starts.
        if abs(n - (originalspiro_cor * spirosize, 0.00)) < 0.01 and loop >= 2:
            main()  # loads menu choice
            break


def add_fav():  # This function adds the digital root of a number to a list
    print(10*x)  # for aesthetics
    global fav
    digi_root_list = []  # list where the name and times table for the inputs a stored
    # asks for what the user wants to name the spirolateral
    spironame = input("What name do you want for the spirolateral? ")
    # asks for the time table that the user wants
    multinum = get_int(2, 20, "What times table do you want from 2-20? ")
    # calls multiplication therefore calling digitroot, finds the digital root for the number entered
    for repeat_num in multiplication(multinum):
        if repeat_num in digi_root_list:  # If the same number repeats in the list then the code will break
            break
        else:
            digi_root_list.append(repeat_num)  # adds repeat_num to digi_root_list
    # inserts the name of the spirolateral in the first slot (0) of the list
    digi_root_list.insert(0, spironame)
    fav.append(digi_root_list)  # appends the digirootlist to the favourites list (fav)
    display_fav()  # displays favourites to show that the spirolateral was added
    main()  # shows the menu choices


def del_fav():  # This function allows you to delete spirolaterals from the favourites list
    print(10*x)  # For aesthetics
    global spirolateral, fav
    num = 1
    if len(fav) > 0:  # Displays favourites list (similar to display_fav)
        for Spirolateralname in fav:
            print(num, Spirolateralname)
            num = num + 1
    else:
        print("sorry there is nothing in list")
        main()
    try:
        # input number minus by one to account for python counting from 0
        deletenum = get_int(
            1, len(fav), "What spirolateral from the favourtites list do you want to delete? ") - 1
        fav.pop(deletenum)  # "pops" input - 1 from the list fav
        print("You just deleted spirolateral", deletenum+1, "from the list")
        main()        # Displays choice menu
    except IndexError:  # if user input is invalid (input = 4 when only 2 items in list)
        print("Sorry that is not a valid option")


def menu_choice():  # This fuction runs first, and lets the user choose what function they want to call
    global items
    rangeitems_ = len(items)  # length of list "items"
    while True:
        print("Please enter a number"
              " for your menu choice 1 to ", rangeitems_)  # Futureproofing as if another item were to be added to the list then the rangeitems_ would automatically calculate how many items are in the list.
        # Depending on user input from 1 - 5 will call associated function
        choice = get_int(1, rangeitems_, "Menu item number ")
        if choice == 1:
            display_fav()
        if choice == 2:
            add_fav()
        if choice == 3:
            draw_spiro()
        if choice == 4:
            del_fav()
        if choice == 5:
            print("Exiting program...")
            sys.exit()  # Easy way of exiting the program without dealing with (while true = true) can help prevent bugs and issues


def main():  # This function calls both display menu and menu_choice
    print(10*x)
    display_menu()
    menu_choice()


main()
