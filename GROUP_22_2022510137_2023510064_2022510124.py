import math

point1 = [6, 148, 72, 35, 0, 33.6, 0.627, 50]
point2 = [1, 85, 66, 29, 0, 26.6, 0.351, 31]

sum_squares = 0

for i in range(len(point1)):
    difference = point1[i] - point2[i]
    sum_squares += difference ** 2

distance = math.sqrt(sum_squares)

print(f"Euclidean Distance: {distance:.3f}")