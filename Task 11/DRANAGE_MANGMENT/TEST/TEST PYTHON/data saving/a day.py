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

# Function to calculate the time until the next day at a specific time
def time_until_next_day(target_time):
    now = datetime.now()
    # Calculate the next occurrence of the target time
    next_day = now + timedelta(days=1)
    next_target_time = next_day.replace(hour=target_time.hour, minute=target_time.minute, second=0, microsecond=0)
    
    # If the target time today has already passed, schedule for tomorrow
    if now > next_target_time:
        next_target_time = next_target_time + timedelta(days=1)
    
    time_remaining = (next_target_time - now).total_seconds()
    return time_remaining

# Main loop to create folders at a daily interval
try:
    # Set the target time for folder creation (e.g., midnight)
    target_time = datetime.strptime("00:00", "%H:%M").time()  # Change this to your desired time

    while True:
        # Calculate the time remaining until the next day at the target time
        time_remaining = time_until_next_day(target_time)
        
        # Sleep until the next day at the target time
        print(f"Waiting for {time_remaining / 3600:.2f} hours until the next folder creation...")
        time.sleep(time_remaining)
        
        # Create the folder at the target time
        create_folder()

except KeyboardInterrupt:
    print("Process stopped by the user.")