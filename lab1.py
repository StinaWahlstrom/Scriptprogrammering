from statistics import mean

pulses = [1601, 1596, 1596, 1598, 1599, 1598, 1598, 1599, 1599, 1599, 1594, 1586, 1572, 1550, 1525, 1503, 1489, 1482,
          1479, 1475, 1470, 1465, 1463, 1471, 1490, 1503, 1516, 1526, 1532, 1536, 1537, 1545, 1553, 1561, 1563, 1561,
          1556, 1550, 1544, 1544, 1545, 1554, 1562, 1566, 1568, 1571, 1576, 1579, 1578, 1581, 1581, 1583, 1583, 1587,
          1585, 1588]

print(pulses)
n = len(pulses)
print(n)



sum = 0

for i in range(n):
    sum = sum + pulses[i]


print(sum)
print(sum/n)

def my_mean_function(value_in):
    sum=0
    n=len(value_in)
    for i in range(n):
        sum = sum + value_in[i]

    value_out = sum/n
    return value_out

print(my_mean_function(pulses[0:10]))

print(mean(pulses))

print(pulses[-1])
print(pulses[0:9])
print( pulses[:5] )

def modulo_function(x):
    length=len(x)
    for i in range(length):
        a = x[i]
        if a % 5 == 0 and i % 7 == 0:
            print ("python", end=" ")
        elif a % 5 == 0:
            print("spam", end=" ")
        elif a % 7 == 0:
            print("eggs", end=" ")
        else:
            print(a, end=" ")



modulo_function(pulses[0:50])