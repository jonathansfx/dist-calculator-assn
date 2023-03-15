# welcome message
print("WELCOME TO THE DISTANCE CALCULATOR!")

# get numbers from user
x1 = float(input("enter the x1 value: "))
y1 = float(input("enter the y1 value: "))
x2 = float(input("enter the x2 value: "))
y2 = float(input("enter the y2 value: "))

# process
dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

# output
print("the distance between these two points is " + str(dist) + ".")
