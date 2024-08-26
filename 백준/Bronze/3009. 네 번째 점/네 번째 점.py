x_coords = []
y_coords = []

for _ in range(3):
    x, y = map(int, input().split())
    x_coords.append(x)
    y_coords.append(y)

x4 = x_coords[0] ^ x_coords[1] ^ x_coords[2]
y4 = y_coords[0] ^ y_coords[1] ^ y_coords[2]

print(x4, y4)
