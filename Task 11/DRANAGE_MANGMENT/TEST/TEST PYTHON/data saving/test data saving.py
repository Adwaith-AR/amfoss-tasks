sensor_data = [
    ["Timestamp", "Sensor Value"],
    ["2024-12-22 10:00:00", 23.5],
    ["2024-12-22 10:01:00", 24.1],
]

# New data to add
new_data = ["2024-12-22 10:02:00", 24.7]

# Append the new data to the list
sensor_data.append(new_data)

# Print the updated list
for row in sensor_data:
    print(row)