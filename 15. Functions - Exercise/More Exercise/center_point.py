import math


def distance():
    point_1_x = float(input())
    point_1_y = float(input())
    point_2_x = float(input())
    point_2_y = float(input())

    distance_to_origin_1 = math.sqrt((point_1_x - 0) ** 2 + (point_1_y - 0) ** 2)
    distance_to_origin_2 = math.sqrt((point_2_x - 0) ** 2 + (point_2_y - 0) ** 2)

    if distance_to_origin_1 <= distance_to_origin_2:
        return f"({math.floor(point_1_x)}, {math.floor(point_1_y)})"
    elif distance_to_origin_2 < distance_to_origin_1:
        return f"({math.floor(point_2_x)}, {math.floor(point_2_y)})"


print(distance())
