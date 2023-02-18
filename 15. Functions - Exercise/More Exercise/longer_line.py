import math
def distance():
    point_1_x = float(input())
    point_1_y = float(input())
    point_2_x = float(input())
    point_2_y = float(input())
    point_3_x = float(input())
    point_3_y = float(input())
    point_4_x = float(input())
    point_4_y = float(input())


    distance_1 = math.sqrt((point_2_x-point_1_x)**2+(point_2_y-point_1_y)**2)
    distance_2 = math.sqrt((point_4_x-point_3_x)**2+(point_4_y-point_3_y)**2)


    if distance_1 >= distance_2:
        return f"({math.floor(point_2_x)}, {math.floor(point_2_y)})({math.floor(point_1_x)}, {math.floor(point_1_y)})" 
    elif distance_2 > distance_1:
        return f"({math.floor(point_4_x)}, {math.floor(point_4_y)})({math.floor(point_3_x)}, {math.floor(point_3_y)})" 

print(distance())