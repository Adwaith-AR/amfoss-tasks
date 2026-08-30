import os
import time
from datetime import datetime, timedelta

# Function to create a folder with the current date and time as the name
def create_folder():
    # Get the current date and time
    now = datetime.now()
    
    # Format the folder name as "YYYY-MM-DD_HH-MM-SS"
    folder_name = now.strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create the folder if it doesn't already exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    else:
        print(f"Folder '{folder_name}' already exists.")

# Function to calculate the time until the next full hour
def time_until_next_hour():
    now = datetime.now()
    next_hour = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
    time_remaining = (next_hour - now).total_seconds()
    return time_remaining

# Main loop to create folders at the top of every hour
try:
    while True:
        # Calculate the time remaining until the next full hour
        time_remaining = time_until_next_hour()
        
        # Sleep until the next full hour
        print(f"Waiting for {time_remaining:.0f} seconds until the next full hour...")
        time.sleep(time_remaining)
        
        # Create the folder at the top of the hour
        create_folder()

except KeyboardInterrupt:
    print("Process stopped by the user.")