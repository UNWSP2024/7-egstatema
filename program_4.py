# Eliya Statema
# 3/6/25
# Coordinates

import math

def get_coordinates(coord_1, coord_2):
    return math.sqrt((coord_2[0] - coord_1[0]) ** 2 +
                     (coord_2[1] - coord_1[1]) ** 2 +
                     (coord_2[2] - coord_1[2]) ** 2)

def main():
    try:
        x1, y1, z1 = map(float, input("Enter the first coordinates (x, y, z): ").split(","))
        coord_1 = (x1, y1, z1)

        x2, y2, z2 = map(float, input("Enter the second coordinates (x, y, z): ").split(","))
        coord_2 = (x2, y2, z2)
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")

    distance = get_coordinates(coord_1, coord_2)
    print(f"The distance between these points is: {distance:.2f}")

if __name__ == "__main__":
    main()