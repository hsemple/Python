# Area calculation program
print "Welcome to the area calculation program"
print "---------------------------------------"
print ""

calculate=1
while calculate != 0:

    # Print out the menu:
    print "Please select a shape:"
    print "1 Rectangle"
    print "2 Circle"

    # Get the user's choice:
    shape = input(">")

    # Calculate the area:
    if shape == 1:


        height = input("Please enter the height: ")
        width = input("Please enter the width: ")
        area = height*width
        geometry = "rectangle"

    else:

        radius = input("Please enter the radius: ")
        area = 3.13*(radius*radius)
        geometry = "Circle"

    print "\nThe area of ", geometry, " is ", area, "\n"
    calculate = input ("Do you want to calculate a area for another shape?(1-Yes|0-No):")


print "\nThank you for using this software!" 
