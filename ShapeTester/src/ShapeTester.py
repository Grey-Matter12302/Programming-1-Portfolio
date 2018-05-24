import Box, Sphere, Pyramid

shape = input("What shape would you like to perform calculations on today? Box - b, Pyramid - p, Sphere - s:")

if (shape == "b"):
    b1 = Box.Box()
    boxLength = int(input("Enter the length of the box:"))
    boxHeight = int(input("Enter the height of the box:"))
    boxWidth = int(input("Enter the width of the box:"))
    print(b1.boxVol())
