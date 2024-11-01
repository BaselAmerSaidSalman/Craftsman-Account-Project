hight = int(input("Enter the hight of your room: \n"))
width = int(input("Enter the width of your room: \n"))
price = int(input("Enter the price of 1m: \n"))
area = hight * width
total_price = area * price
print("Your Area is " + str(area) + " m^2")
print("Your total price is " + str(total_price) + "$")