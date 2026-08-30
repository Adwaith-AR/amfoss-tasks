from openpyxl import Workbook

# Sample sensor data
sensor_data = [
    ["Timestamp", "Sensor Value"],
    ["2024-12-22 10:00:00", 23.5],
    ["2024-12-22 10:01:00", 24.1],
]

# Create a workbook and select the active worksheet
wb = Workbook()
ws = wb.active
ws.title = 'sensor data '

# Write data to the worksheet
for row in sensor_data:
    ws.append(row)

# Save the Excel file
wb.save("sensor_data.xlsx")
print("Data saved to sensor_data.xlsx")



