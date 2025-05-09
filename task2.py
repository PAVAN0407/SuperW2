import re
def is_vaild_email(email):
    pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email ) is not None
print(is_vaild_email("example@gmail.com"))
print(is_vaild_email("example@gmail"))

