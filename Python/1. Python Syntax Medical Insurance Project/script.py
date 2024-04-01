# Assign values for individual's characteristics
age = 28  # age of the individual in years
sex = 0  # 0 for female, 1 for male*
bmi = 26.2  # individual’s body mass index
num_of_children = 3  # number of children the individual has
smoker = 0  # 0 for a non-smoker, 1 for a smoker

# Calculate initial insurance cost based on individual's characteristics
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# Increase BMI by 3.1 and recalculate insurance cost
bmi += 3.1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# Calculate the change in insurance cost after increasing BMI
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.")

# Reset BMI and change sex to male, then recalculate insurance cost
bmi = 26.2
sex = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# Calculate the change in insurance cost for being male instead of female
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")
