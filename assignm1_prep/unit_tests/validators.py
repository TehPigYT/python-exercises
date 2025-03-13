def is_valid_email(email):
    if "@" in email and (email.endswith(".gr") or email.endswith(".com")):
        return True
    return False
