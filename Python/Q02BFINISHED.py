# Q02b

time = 0
initialSpeed = 5
acceleration = 2.75
newSpeed = 0
distance = 0

while (time < 4):
    newSpeed = initialSpeed + time * acceleration
    distance = 0.5 * time * (newSpeed + initialSpeed)
    time = time + 1


print(distance)
