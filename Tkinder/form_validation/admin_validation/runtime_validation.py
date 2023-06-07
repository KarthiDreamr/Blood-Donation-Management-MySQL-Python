def atmost_fifty_char_onlyalpha_ensure(input):
    return len(input) <= 50 or input == "" and input.isalpha()


def atleast_eight_atmost_thirtychar_ensure(input):
    return len(input) <= 30 and len(input) >= 8 or input == ""

