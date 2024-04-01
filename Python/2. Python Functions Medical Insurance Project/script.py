# Define the function to calculate insurance cost
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
    print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")
    return estimated_cost

# Calculate insurance cost for Maria
maria_insurance_cost = calculate_insurance_cost(28, 0, 26.2, 3, 0, name="Maria")

# Calculate insurance cost for Omar
omar_insurance_cost = calculate_insurance_cost(35, 1, 22.2, 0, 1, name="Omar")
