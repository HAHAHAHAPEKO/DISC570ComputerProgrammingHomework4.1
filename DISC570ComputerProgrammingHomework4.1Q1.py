a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant: "))
#flag to detect scenarios of the equation
flag = True
while a != 0 and b != 0:
    while b**2 - (4*a*c) >= 0:
        temp = (b**2 - 4*a*c)**0.5
        x1 = (-b + temp)/2*a
        x2 = (-b - temp)/2*a
        flag = False
        print(f"The first solution is x1 = {x1}")
        print(f"The second solution is x2 = {x2}")
        break
    if flag == True:
        print("No real roots in your equation")
        flag = False
    break
if flag == True:
    print("The coefficient of x^2 and x cannot be 0.")

