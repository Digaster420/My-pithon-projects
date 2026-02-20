number1 = float(input("Write your first number here: "))
number2 = float(input("Write your second number here: "))
number3 = float(input("Write your third number here: "))
if number1 > number2 and number1 > number3:
    print("Your first number is the biggest!")
elif number2 >number1 and number2 > number3:
    print ("Your second number is the biggest!")
elif number3 > number1 and number3 > number2:
    print("Your third number is the biggest!")
    