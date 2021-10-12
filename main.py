# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
add_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

price = 15 if size == "S" else 20 if size == "M" else 25 if size == "L" else print("Please enter valid input")

if size == "S" and add_pepperoni == "Y":
  extra_pepperoni = 2
elif (size == "M" or size == "L") and add_pepperoni == "Y":
  extra_pepperoni = 3
elif (size == "S" or "M" or "L") and add_pepperoni == "N":
  extra_pepperoni = 0
else:
  print("Please enter valid input")

if (size == "S" or "M" or "L") and add_cheese == "Y":
  extra_cheese = 1
elif (size == "S" or "M" or "L") and add_cheese == "N":
  extra_cheese = 0
else:
  print("Please enter valid input")

print("Your final bill is: $%s." %(price+extra_pepperoni+extra_cheese))







