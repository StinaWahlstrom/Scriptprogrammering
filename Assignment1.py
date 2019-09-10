import matplotlib.pyplot as plt
VOLTAGE_CONVERSION: float = ((2 ^ 10) - 1) * 0.6

# Question 1
# Read in data:
with open('pulses.csv', 'r') as pulses:
    lines = pulses.readlines()
    rows = len(lines)


# Reformat into voltages
def voltage_converter(x):
    x = float(x)
    return x / VOLTAGE_CONVERSION


# Create empty vectors:
timestamps = []
detector_readings = []

# Add data to new vectors:
for i in range(rows):
    line = lines[i]
    line_column = line.split(',')

    timestamps.insert(i, line_column[0])
    line_column.pop(0)
    row_length = len(line_column)
    for j in range(row_length):
        line_column[j] = voltage_converter(line_column[j])

    detector_readings.insert(i, line_column)

plt.plot(detector_readings[3])
plt.show()