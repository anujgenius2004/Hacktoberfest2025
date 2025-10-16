
# This function calculates the area of a rectangle
# It takes two parameters: width and height
def calculate_area(width, height):
    """
    Calculates and returns the area of a rectangle.
    Area = width * height
    """
    area = width * height
    return area

# --- Example Usage ---

# 1. Define the dimensions
rect_width = 10
rect_height = 5

# 2. Call the function with the defined dimensions
result_area = calculate_area(rect_width, rect_height)

# 3. Print the result
print(f"Rectangle Width: {rect_width}")
print(f"Rectangle Height: {rect_height}")
print(f"The calculated area is: {result_area}")

# Another example:
print(f"\nArea of a 7x3 rectangle: {calculate_area(7, 3)}")
