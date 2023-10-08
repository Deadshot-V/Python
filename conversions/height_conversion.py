def convert_height(height, from_unit, to_unit):
    """
    Convert a height from one unit to another.

    Args:
        height (float): The height value to convert.
        from_unit (str): The source unit (e.g., 'cm', 'inches', 'feet').
        to_unit (str): The target unit (e.g., 'cm', 'inches', 'feet').

    Returns:
        float: The converted height value.

    Examples:
        >>> convert_height(180, 'cm', 'inches')
        70.8661417

        >>> convert_height(5.9, 'feet', 'cm')
        179.832

        >>> convert_height(70, 'inches', 'feet')
        5.8333333
    """
    if from_unit == to_unit:
        return height

    # Define conversion factors
    unit_factors = {
        'cm': 2.54,      # 1 inch = 2.54 cm
        'inches': 0.3937,  # 1 cm = 0.3937 inches
        'feet': 0.0328    # 1 foot = 30.48 cm
    }

    # Perform the conversion
    converted_height = height * unit_factors[from_unit] / unit_factors[to_unit]
    return converted_height

if __name__ == "__main__":
    import doctest
    doctest.testmod()
