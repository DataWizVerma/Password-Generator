import random
import string
import os
from datetime import datetime

# Function to generate a strong password based on the input text
def generate_strong_password(input_text):
    # Ensure the input text is not empty
    if not input_text:
        return "Input text is empty. Cannot generate password."

    # Add random characters to make the password strong
    random_characters = random.choices(string.ascii_letters + string.digits + string.punctuation, k=8)

    # Combine the input text with the random characters
    combined_text = input_text + ''.join(random_characters)

    # Shuffle the characters to make the password more unpredictable
    password = ''.join(random.sample(combined_text, len(combined_text)))

    return password

# Take input from the user
thing_name = input("Enter the name of the thing for which you need a password (e.g., Email, Bank Account): ")
input_text = input("Enter some text to create a strong password: ")

# Generate the password
password = generate_strong_password(input_text)

# Get the current date and time of password creation
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")  # Replacing ':' with '-'

# Define the folder where the password file will be saved
folder_path = r"F:\Password Gen"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)  # Create the folder if it doesn't exist

# Create a file name based on the thing_name and timestamp
file_name = f"{thing_name.replace(' ', '_')}_password_{current_datetime}.txt"
file_path = os.path.join(folder_path, file_name)

# Save the thing name, password, and the date/time to a text file
with open(file_path, "w") as file:
    file.write(f"Thing: {thing_name}\n")
    file.write(f"Password: {password}\n")
    file.write(f"Generated on: {current_datetime}\n")

print(f"Your strong password for {thing_name} is: {password}")
print(f"The password has been saved to '{file_path}'")
