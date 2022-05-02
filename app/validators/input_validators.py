import re


def validate_integer_or_str(item):
    return validate_integer(item) or validate_string(item)


def validate_string(string):
    if type(string) != str:
        return False
    if string is None or string.replace(" ", "")=='':
        return False
    return True
    
    
def validate_integer(integer):
    
    if integer is None:
        return False
    
    if type != int:
        if type==str:
            if not integer.isdigit():
                return False
    return True  
    
    
def validate_email(email):
    
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if email is None:
        return False
    if type(email) != str:
        return False   
    return re.search(regex,email)


def validate_phone_number(phone_number):
    
    regex = r"\(?\d{4}\)?[-.\s]\d{3}[-.\s]\d{3}"
    if phone_number is None:
        return False
    if type(phone_number) != str:
        return False   
    return re.search(regex,phone_number)