import math
import matplotlib.pyplot as plt
#
# with open('EbbasData_clean.csv', 'r') as ebba:
#     lines = ebba.readlines()
# length = len(lines)
#
# times = []
# pressures_abs = []
# temps = []
# volumes = []
#
# for i in range(length):
#
#     if i > 3 and i < 244:
#         line = lines[i]
#         linecolumn = line.split(',')
#
#         if linecolumn[2] == '':
#             linecolumn[2] = math.nan
#         else:
#             linecolumn[2] = float(linecolumn[2])
#
#         if linecolumn[3] == '':
#             linecolumn[3] = math.nan
#         else:
#             linecolumn[3] = float(linecolumn[3])
#
#         if linecolumn[4] == '':
#             linecolumn[4] = math.nan
#         else:
#             linecolumn[4] = float(linecolumn[4])
#
#         if linecolumn[10] == '':
#             linecolumn[10] = math.nan
#         else:
#             linecolumn[10] = float(linecolumn[10])
#
#         times.insert(i, linecolumn[2])
#         pressures_abs.insert(i, linecolumn[3])
#         temps.insert(i, linecolumn[4])
#         volumes.insert(i, linecolumn[10])
#
# lenTi = len(times)
# lenPr = len(pressures_abs)
# lenTe = len(temps)
# lenVo = len(volumes)
#
# print(lenTi, lenPr, lenTe, lenVo)


def read_function(column):
    with open('EbbasData_clean.csv', 'r') as ebba:
        lines = ebba.readlines()
        length = len(lines)

        values = []

    for i in range(250):

        if i > 3 and i < 244:
            line = lines[i]
            linecolumn = line.split(',')

            if linecolumn[column] == '':
                linecolumn[column] = math.nan
            else:
                linecolumn[column] = float(linecolumn[column])

            values.insert(i - 2, linecolumn[column])

    return values


temps = read_function(3)
times = read_function(1)
pressures =read_function(2)
volumes = read_function(10)

plt.figure()
plt.plot(volumes, pressures)
plt.suptitle('Tests')
plt.xlabel('Volume(mÂ³)')
plt.ylabel('Pressure(kPa)')
plt.show()

plt.figure()
plt.plot(times, temps, times, pressures, times, volumes)
plt.suptitle('Tests')
plt.xlabel('Times(s)')
plt.ylabel('y-values')
plt.legend(('Temperature(Â°C)', 'Pressure(kPa)', 'Volume(mÂ³)'),
           loc='upper right')
plt.show()


