
#TO CHECK WHETHER A TRIANGLE IS RIGHT ANGLED OR NOT!!!

P = int(input('Enter length of perpendicular :'))
B = int(input('Enter length of base :'))
H = int(input('Enter length of hypotenuse :'))

def right_angle_triangle(P, B, H):
    if P**2 + B**2 == H**2:
        print("THE TRIANGLE IS RIGHT ANGLE TRAINGLE!")
    else:
        print("THE TRIANGLE IS NOT A RIGHT ANGLE TRAINGLE!")

right_angle_triangle(P, B, H)


