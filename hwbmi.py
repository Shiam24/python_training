height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
               
bmi = weight / (height ** 2)


print(f"Your BMI is: {bmi:.2f}")


if bmi < 18.5:
    print("You are Underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have Normal weight.")
elif 25 <= bmi < 29.9:
    print("You are Overweight.")
else:
    print("You are Obese.")