import math

def generate_path():
    current_angle = 45
    pos_x, pos_y = 0, 0
    path_points = [(pos_x, pos_y)]

    for _ in range(7):
        pos_x += 5 * math.sin(math.radians(current_angle))
        pos_y += 5 * math.cos(math.radians(current_angle))
        path_points.append((pos_x, pos_y))

        current_angle += 45

        pos_x += 10 * math.sin(math.radians(current_angle))
        pos_y += 10 * math.cos(math.radians(current_angle))
        path_points.append((pos_x, pos_y))

        current_angle += 135

    return path_points

def count_lattice_points(points):
    total_area = 0
    boundary_points_count = 0

    for idx in range(len(points)):
        x_start, y_start = points[idx]
        x_end, y_end = points[(idx + 1) % len(points)]

        total_area += x_start * y_end - x_end * y_start

        boundary_points_count += math.gcd(int(abs(x_end - x_start)), int(abs(y_end - y_start)))

    total_area = abs(total_area) / 2
    internal_points = total_area + 1 - boundary_points_count / 2
    return int(internal_points)

path = generate_path()
result = count_lattice_points(path)
print(result)