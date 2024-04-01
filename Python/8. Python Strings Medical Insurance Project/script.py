# Original medical data
medical_data = """Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Replace '#' with '$' in medical data
updated_medical_data = medical_data.replace("#", "$")
print(updated_medical_data)

# Count the number of medical records
num_records = 0
for character in updated_medical_data:
    if character == "$":
        num_records += 1 
print("There are " + str(num_records) + " medical records in the data.")

# Split medical data into individual records
medical_data_split = updated_medical_data.split(";")
print(medical_data_split)

# Split each record into individual components and remove extra whitespaces
medical_records = []
for medical_record in medical_data_split:
    medical_records.append(medical_record.split(","))
print(medical_records)

# Clean up each record by stripping extra whitespaces
medical_records_clean = []
for medical_record in medical_records:
    record_clean = []
    for record in medical_record:
        record_clean.append(record.strip())
    medical_records_clean.append(record_clean)
print(medical_records_clean)

# Extract names, ages, BMIs, and insurance costs from cleaned records
names = []
ages = []
bmis = []
insurance_costs = []

for medical_record in medical_records_clean:
    names.append(medical_record[0])
    ages.append(medical_record[1])
    bmis.append(medical_record[2])
    insurance_costs.append(medical_record[3])
print(names)
print(ages)
print(bmis)
print(insurance_costs)

# Calculate the average BMI
total_bmi = 0
for bmi in bmis:
    total_bmi += float(bmi)

average_bmi = total_bmi / len(bmis)
print("Average BMI: " + str(round(average_bmi, 2)))
