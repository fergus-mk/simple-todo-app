from email_validator import validate_email, EmailNotValidError
from app.responses.fail_response import email_not_valid, name_not_alpha, wrong_len_response

def check_email_is_valid(email: str):
    """Checks if email is valid with characters both sides of an '@' symbol"""
    try:
        validation = validate_email(email)
        email = validation.email
    except EmailNotValidError as e:
        return email_not_valid(e)
    
def check_name_is_valid(name: str):
    """Checks if name string has only alpha characters and is 2-50 characters long"""
    if not name.isalpha():
        return name_not_alpha()
    elif len(name) <2:
        return wrong_len_response(choice="short", type_describe="Name")
    elif len(name)>50:
        return wrong_len_response(choice="long", type_describe="Name")
    else:
        pass