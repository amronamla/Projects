# Creating lists of names and corresponding insurance costs
names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Adding a new name and corresponding insurance cost to the lists
names.append("Priscilla")
insurance_costs.append(8320.0)

# Creating a list of tuples by combining names and insurance costs
medical_records = list(zip(insurance_costs, names))
print(medical_records)

# Calculating the number of medical records
num_medical_records = len(medical_records)
print("There are " + str(num_medical_records) + " medical records.")

# Retrieving and printing the first medical record
first_medical_record = medical_records[0]
print("Here is the first medical record: " + str(first_medical_record))

# Sorting the medical records based on insurance costs
medical_records_sorted = sorted(medical_records)
print("Here are the medical records sorted by insurance cost: " + str(medical_records_sorted))

# Extracting the three cheapest insurance costs from the sorted list
cheapest_three = medical_records_sorted[:3]
print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three))

# Extracting the three most expensive insurance costs from the sorted list
priciest_three = medical_records_sorted[-3:]
print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three))

# Counting the occurrences of the name "Paul" in the list
occurrences_paul = names.count("Paul")
print("There are " + str(occurrences_paul) + " individuals with the name Paul in our medical records. ")
