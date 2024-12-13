# If statements
temparature = 25

if temparature > 30:
    print("It's very hot")
    print("Drink plenty of water!")
elif temparature > 20:
    print("It's a nice day")
elif temparature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print("Done")

### Exercise
# Ask user for weight
# Check if it is in Kg or Lb

weight = float(input("Enter your weight: "))
unit = input("(K)g or (L)b: ")

if unit == "K" or unit == "k":
    conv = weight * 2.205
    print("Your weight is " + str(conv) + "Lb")
elif unit == "L" or unit == "l":
    conv = weight / 2.205
    print("Your weight is " + str(conv) + "Kg")
else:
    print("Please enter a valid unit (L or K)")