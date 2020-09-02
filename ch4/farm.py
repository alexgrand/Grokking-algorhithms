def divide_to_squares(length, width):
    modulo = length % width
    
    if modulo == 0:
        return width
    else:
        return divide_to_squares(width, modulo)

length = 1680
width = 640
biggest_square_side = divide_to_squares(length, width)

print(f"В наделе длиной {length}м и шириной {width}м будет {length * width / pow(biggest_square_side, 2)} квадратов со стороной {biggest_square_side}м")