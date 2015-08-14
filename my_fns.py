def normalize_rectangle(rect):
    '''Takes the coordinates (x0, y0, x1, y1) for a rectangle and returns the
    coordinates for a rectangle with sides having the same ration but with the
    lower left corner at the origin and rescaled so the longest side has unit
    length.'''
    x0, y0, x1, y1 = rect   # Unpack the coordinates in rect into separate
                            # variables
    dx = x1 - x0    # Width
    dy = y1 - y0    # Height

    if dx > dy:
        scaled = float(dx) / dy # This calculation is incorrect, and we need to
                                # write a test to identify this.
        upper_x, upper_y = 1.0, scaled
    else:
        scaled = float(dx) / dy
        upper_x, upper_y = scaled, 1.0

    return (0, 0, upper_x, upper_y)

def fahr_to_kelvin(temp):
    '''Takes a temperature in Fahrenheit and returns the corresponding
    temperature in Kelvin.'''
    return ( (temp - 32) * (5.0 / 9) ) + 273.15
