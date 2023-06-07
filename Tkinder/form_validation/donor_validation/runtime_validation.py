def atmost_twenty_char_onlyalpha_ensure(input):
    return input.isalpha() and len(input) <= 20 or input == ""

def atleast_twelve_digit_ensure(input):
    return input.isdigit() and len(input) <= 12 or input == ""

def date_of_birth_ensure(input):
    return len(input) <= 10 or input == ""

def atmost_fifty_char_ensure(input):
    return input.isalpha() and len(input) <= 20 or input == ""

def atmost_thirty_char_ensure(input):
    return len(input) <= 30 or input == ""

def atmost_twenty_char_ensure(input):
    return len(input) <= 20 or input == ""

def atmost_plus_three_char_ensure(input):
    if(input!=""):
        if(len(input)<=3):
            if(len(input)==1 and input[0]=='+'):
                return True

            elif(len(input)==2 and input[0]=='+' and input[1].isdigit()):
                return True
        
            elif(len(input)==3 and input[0]=='+' and input[1].isdigit() and input[2].isdigit() ):
                return True
        
            return False
        
        
        return False
    
    return True

def atmost_thirty_char_onlyalpha_ensure(input):
    return len(input) <= 30 or input == "" and input.isalpha()

def atleast_ten_digit_ensure(input):
    return input.isdigit() and len(input) <= 10 or input == ""

def isdigit_ensure(input):
    return input.isdigit() or input == ""

def atmost_thirtychar_ensure(input):
    return len(input) <= 30 or input == ""