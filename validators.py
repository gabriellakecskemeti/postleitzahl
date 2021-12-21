def input_postal_code(prompt, *postalcodes):
    number = 0
    while True:
        try:
            number_char = input(f"{prompt}")
            # if Q  oder q

            # number= char in zahl  umwandeln
            # *postalcodes schauen
            break
        except ValueError:
            print("Only numbers, please!")

    return number


def _check_postalcode(value, postalcodes):
    print("hello")
