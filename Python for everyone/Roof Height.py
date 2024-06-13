def roof_height(height):
    height = float(input("Enter the height "))
    if height >= 0.0 or height <= 5.0:
        return 3.0 + height * (3) / 5.0
    elif height >= 5.0 or height <= 10.0:
        return 3.0 + (10 - height) * (3) / 5.0
    else:
        return 0