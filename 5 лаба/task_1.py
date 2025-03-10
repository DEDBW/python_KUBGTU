import re

EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

def is_valid_email(email: str) -> bool:
    return EMAIL_REGEX.fullmatch(email) is not None

def get_email_or_raise(email: str) -> str:
    if is_valid_email(email):
        return email
    raise ValueError("Некорректный адрес электронной почты")

if __name__ == '__main__':
    email_input = input("Введите адрес электронной почты: ")
    try:
        valid_email = get_email_or_raise(email_input)
        print("Введённый адрес корректен:", valid_email)
    except ValueError as e:
        print(e)
