def input_postal_code(prompt, *postalcodes):
    number = 0
    s_postalcodes = set(postalcodes)
    while True:
            number_char = input(f"{prompt}")
            if number_char.upper() == "Q":
                return "Good bye!"
            number = _check_postalcode(number_char, s_postalcodes)
            if number is not None:
                return number


def _check_postalcode(value, postalcodes):
    try:
        number = int(value)
    except ValueError:
        print("Only numbers, please!")
        return
    for x in postalcodes:
        if number == x:
            return number
    return
