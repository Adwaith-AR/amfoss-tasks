from datetime import datetime
import time
# Get the current date and time
now = datetime.now()

# Format the date and time
formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_date_time)

# Custom format
custom_format = now.strftime("%A, %B %d, %Y %I:%M %p")
print("Custom format:", custom_format)