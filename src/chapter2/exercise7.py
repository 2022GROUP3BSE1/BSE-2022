money = float(input('Enter the amount to make change for: '))
dollar_20 = money//20
print(dollar_20," twenties")

remainder = money%20
dollar_10 = remainder//10
print(dollar_10," tens")

remainder_2 = remainder%10
dollar_5 = remainder_2//5
print(dollar_5," five")

remainder_3 = remainder_2%5
dollar_1 = remainder_3//1
print(dollar_1," ones")

remainder_4 = remainder_3%1
quarter = remainder_4//0.25
print(quarter," quarters")

remainder_5 = remainder_4%0.25
Dime = remainder_5//0.1
print(Dime," dimes")

remainder_6 = remainder_5%0.1
Nickel = remainder_6//0.05
print(Nickel," nickels")

remainder_7 = remainder_6%0.05
Pennies = remainder_7//0.01
print(Pennies," pennies")