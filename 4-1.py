def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left >= distance_to_pump/ mpg >= 0:
        return (1)
    else:
        return (0)