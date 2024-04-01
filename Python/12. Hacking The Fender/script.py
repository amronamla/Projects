# Import CSV and JSON module
import csv
import json

# List to store compromised usernames
compromised_users = []

# Open the CSV file containing passwords
with open("passwords.csv") as password_file:
    # Read the CSV file as a dictionary
    password_csv = csv.DictReader(password_file)
    
    # Iterate through each row in the CSV file
    for password_row in password_csv:
        # Add the username to the list of compromised users
        compromised_users.append(password_row['Username'])

# Write the list of compromised users to a text file
with open("compromised_users.txt", "w") as compromised_user_file:
    for compromised_user in compromised_users:
        compromised_user_file.write(compromised_user)

# Create a JSON file with a boss message
with open("boss_message.json", "w") as boss_message:
    # Create a dictionary for the boss message
    boss_message_dict = {
        "recipient": "The Boss",
        "message": "Mission Success"
    }
    # Write the boss message dictionary to the JSON file
    json.dump(boss_message_dict, boss_message)

# Write a multi-line string with ASCII art to a CSV file
with open("new_passwords.csv", "w") as new_passwords_obj:
    slash_null_sig = """
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/

"""
    # Write the ASCII art to the CSV file
    new_passwords_obj.write(slash_null_sig)
