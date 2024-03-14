def calculate_bmi(height, weight):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    height_input = input("Enter your height in meters: ")
    weight_input = input("Enter your weight in kilograms: ")

    if height_input.replace('.', '', 1).isdigit() and weight_input.replace('.', '', 1).isdigit():
        height = float(height_input)
        weight = float(weight_input)
        bmi = calculate_bmi(height, weight)
        classification = classify_bmi(bmi)
        print("Your BMI is:", round(bmi, 2))
        print("You are classified as:", classification)
    else:
        print("Please enter valid numerical values for height and weight.")

if __name__ == "__main__":
    main()
