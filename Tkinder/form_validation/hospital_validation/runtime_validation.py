def isdigit_ensure(input):
    return input.isdigit() or input == ""

def atmost_thirty_char_onlyalpha_ensure(input):
    return len(input) <= 30 or input == "" and input.isalpha()

def atmost_thirty_char_ensure(input):
    return len(input) <= 30 or input == ""

def isdigit_atmost_fourhundred_ensure(input):
    return input.isdigit() and input<50 or input == ""

def atleast_ten_digit_ensure(input):
    return input.isdigit() and len(input) <= 10 or input == ""

def atmost_twenty_char_onlyalpha_ensure(input):
    return len(input) <= 20 or input == "" and input.isalpha()

def isdigit_atmost_fifty_ensure(input):
    return (input.isdigit() and int(input)<=50 ) or input == ""
