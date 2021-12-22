def input_postal_code(prompt, *postalcodes):
    number = 0
    while True:
        number_char = input(f"{prompt}")
        if number_char.upper() == "Q":
            return "Good bye!"
        number = _check_postalcode(number_char, postalcodes)
        if number is not None:
            return number_char


def _check_postalcode(value, postalcodes):
    try:
        number = int(value)
    except ValueError:
        print("Only numbers, please!")
        return
    try:
        return postalcodes.index(number)
    except ValueError:
        print(f"Postal code {number} is not valid! Valid codes are: {postalcodes}")
        return
