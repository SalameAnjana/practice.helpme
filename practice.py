def print_pattern(n):
    for i in range(1, n + 1):
        print('*' * i)

# Example Usage
number = 4
print_pattern(number)

def calculate_area(base, height, shape_type):
    if shape_type == "triangle":
        return 1/2 * base * height
    elif shape_type == "rectangle":
        return length * breath
    else:
        return "Invalid shape type. Please use 'triangle' or 'rectangle'."
    
number = 3
print_pattern(number)

base = 12
height = 22
length = 5
breath = 3

triangle_area = calculate_area(base, height, "triangle")
print(f"The area of triangle is {triangle_area}")

rectangle_area = calculate_area(length, breath, "rectangle")
print(f"The area of the rectangle is {rectangle_area}")

print_pattern(4)

