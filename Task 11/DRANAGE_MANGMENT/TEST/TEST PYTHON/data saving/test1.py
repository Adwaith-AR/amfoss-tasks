import os
from datetime import datetime, timedelta

# Function to create a folder with the current date and time as the name
def create_folder():
    # Get the current date and time
    now = datetime.now()
    
    # Format the folder name as "YYYY-MM-DD_HH-MM-SS"
    folder_name = now.strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create the folder
    os.makedirs(folder_name)
    print(f"Folder '{folder_name}' created successfully.")

# Main loop to create folders at 1-hour intervals
try:
    # Initialize the last folder creation time
    last_creation_time = datetime.now()
    print (datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    while True:
        # Get the current time
        current_time = datetime.now()

        # Check if 1 hour has passed since the last folder creation
        if current_time - last_creation_time >= timedelta(milliseconds=100000):
            create_folder()  # Create a folder
            last_creation_time = current_time  # Update the last creation time
        

except KeyboardInterrupt:
    print("Process stopped by the user.")
