#digit
def isdigit_ensure(input):
    if(input!=""):
        return True
    return input.isdigit()

def isdigit_atmost_fourhundred_ensure(input):
    if(input!=""):
        return True
    return input.isdigit() and int(input) <= 400

def isdigit_atmost_fifty_ensure(input):
    if(input!=""):
        return True
    return (input.isdigit() and int(input)<=50 )

def atmost_ten_digit_ensure(input):
    if(input!=""):
        return True
    return input.isdigit() and len(input) <= 10

#street name
def atmost_fifty_char_ensure(input):
    if(input!=""):
        return True
    return input.isalpha() and len(input) <= 50

def atmost_twelve_digit_ensure(input):
    if(input!=""):
        return True
    return input.isdigit() and len(input) <= 12


def atmost_thirty_char_onlyalpha_ensure(input):
    if(input!=""):
        return True
    return len(input)>30 and input.isalpha()

def atmost_thirty_char_ensure(input):
    if(input!=""):
        return True
    return len(input) <= 30




def date_of_birth_ensure(input):
    if(input!=""):
        return True
    return len(input) <= 10


#character
def atmost_twenty_char_ensure(input):
    if(input!=""):
        return True
    return len(input) <= 20

def atmost_plus_three_char_ensure(input):
    if(input!=""):
        return True
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

def atmost_fifty_char_onlyalpha_ensure(input):
    if(input!=""):
        return True
    return len(input) <= 50 and input.isalpha()

