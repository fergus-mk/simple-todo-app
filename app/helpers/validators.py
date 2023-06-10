import re
from email_validator import validate_email, EmailNotValidError

from .responses import fail_response

def check_email_is_valid(email: str):
    """Checks if email is valid with characters both sides of an '@' symbol"""
    try:
        validation = validate_email(email)
        email = validation.email
    except EmailNotValidError as e:
        return fail_response.email_not_valid(e)
    
def check_name_is_valid(name: str):
    """Checks if name string has only alpha characters and is 2-50 characters long"""
    if not name.isalpha():
        return fail_response.name_not_alpha()
    elif len(name) <2:
        return fail_response.wrong_len_response(choice="short", type_describe="Name")
    elif len(name)>50:
        return fail_response.wrong_len_response(choice="long", type_describe="Name")
    else:
        pass

def check_password_is_valid(password: str):
    """Checks if password is at least 5 characters, contains a digit and a special character."""
    if len(password) < 5:
        return fail_response.password_not_valid()
    
    elif not re.search(r'\d', password):
        return fail_response.password_not_valid()
    elif not re.search(r'\W', password):
        return fail_response.password_not_valid()
    else:
        pass

def check_all_fields(user_data):
    """Checks if all fields contained in user data"""
    required_fields = ["email", "first_name", "last_name", "password"]
    missing_fields = [field for field in required_fields if field not in user_data]

    if missing_fields:
        fail_response.missing_user_fields_error()
    else:
        pass

def check_todo_content_is_valid(content: str):
    """Checks if content of todo is 2-200 characters long"""
    if len(content) <2:
        return fail_response.wrong_len_response(choice="short", type_describe="Content")
    elif len(content) >200:
        return fail_response.wrong_len_response(choice="long", type_describe="Content")
    else:
        pass

def check_todo_priority_is_valid(priority: int):
    """Checks if todo is an intger from 0-5"""
    if priority <0:
        return fail_response.priority_out_of_range()
    elif priority >5:
        return fail_response.priority_out_of_range()
    else:
        pass
    