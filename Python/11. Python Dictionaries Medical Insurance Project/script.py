# Create an empty dictionary to store medical costs
medical_costs = {}

# Add initial costs for Marina and Vinay
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0

# Update the dictionary with additional costs for Connie, Isaac, and Valentina
medical_costs.update({
  "Connie": 8886.0,
  "Isaac": 16444.0,
  "Valentina": 6420.0
})
print(medical_costs)

# Update Vinay's medical cost
medical_costs["Vinay"] = 3325.0
print(medical_costs)

# Calculate the total and average medical costs
total_cost = 0
for cost in medical_costs.values():
  total_cost += cost

average_cost = total_cost / len(medical_costs)
print("Average Insurance Cost: " + str(average_cost))

# Create lists for names and ages
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

# Zip names and ages into a dictionary
zipped_ages = zip(names, ages)
names_to_ages = {key: value for key, value in zipped_ages}
print(names_to_ages)

# Retrieve Marina's age from the dictionary
marina_age = names_to_ages.get("Marina", "None")
print("Marina's age is " + str(marina_age))

# Create a nested dictionary for medical records
medical_records = {
  "Marina": {
    "Age": 27, 
    "Sex": "Female", 
    "BMI": 31.1,
    "Children": 2, 
    "Smoker": "Non-smoker",
    "Insurance_cost": 6607.0
  },
  "Vinay": {
    "Age": 24, 
    "Sex": "Male", 
    "BMI": 26.9,
    "Children": 0, 
    "Smoker": "Non-smoker",
    "Insurance_cost": 3225.0
  },
  "Connie": {
    "Age": 43, 
    "Sex": "Female", 
    "BMI": 25.3	,
    "Children": 3, 
    "Smoker": "Non-smoker",
    "Insurance_cost": 8886.0
  },
  "Isaac": {
    "Age": 35, 
    "Sex": "Male", 
    "BMI": 20.6,
    "Children": 4, 
    "Smoker": "Smoker",
    "Insurance_cost": 16444.0
  },
  "Valentina": {
    "Age": 52, 
    "Sex": "Female", 
    "BMI": 18.7,
    "Children": 1, 
    "Smoker": "Non-smoker",
    "Insurance_cost": 6420.0
  }
}
print(medical_records)

# Print Connie's insurance cost from the nested dictionary
print("Connie's insurance cost is " + str(medical_records["Connie"]["Insurance_cost"]) + " dollars.")

# Remove Vinay from the medical records
medical_records.pop("Vinay")

# Iterate through medical records and print information
for name, record in medical_records.items():
  print(name + " is a " + str(record["Age"]) + \
  " year old " + record["Sex"] + " " + record["Smoker"] \
  + " with a BMI of " + str(record["BMI"]) + \
  " and insurance cost of " + str(record["Insurance_cost"]))
