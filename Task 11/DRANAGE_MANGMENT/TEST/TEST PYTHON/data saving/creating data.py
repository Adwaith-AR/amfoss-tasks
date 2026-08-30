sensor_data = [
    ["Timestamp", "Sensor Value"],
    ["2024-12-22 10:00:00", 23.5],
    ["2024-12-22 10:01:00", 24.1],
]

# Create a new row
new_row = ["2024-12-22 10:02:00", 24.7]

# Add the new row to sensor_data
sensor_data.append(new_row)

# Print the updated sensor_data
for row in sensor_data:
    print(row)