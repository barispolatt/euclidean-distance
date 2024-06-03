import math

# 1. Noktaların tanımlanması
points = [
    (1, 2),
    (4, 6),
    (5, 3),
    (7, 8),
    (2, 1)
]

# 2. Öklid mesafesi için bir fonksiyon yazma
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# 3. Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# 4. Minimum mesafenin bulunması
min_distance = min(distances)
print("Minimum Öklid mesafesi:", min_distance)
