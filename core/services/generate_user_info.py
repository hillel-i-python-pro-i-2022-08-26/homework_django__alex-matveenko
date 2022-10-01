from faker import Faker

from users_generator.models import UserInfo

fake = Faker()


def generate_names(amount: int) -> list[str]:
    name_list: list[str] = []
    for name in range(amount):
        name = fake.name()
        if name in name_list:
            continue
        name_list.append(name)
    return name_list


def generate_emails(amount: int) -> list[str]:
    email_list: list[str] = []
    for email in range(amount):
        email = fake.email()
        if email in email_list:
            continue
        email_list.append(email)
    return email_list


def generate_passwords(amount: int) -> list[str]:
    password_list: list[str] = []
    for password in range(amount):
        password = fake.password()
        if password in password_list:
            continue
        password_list.append(password)
    return password_list


def organize_info(amount: int) -> UserInfo:
    names = generate_names(amount=amount)
    emails = generate_emails(amount=amount)
    passwords = generate_passwords(amount=amount)

    for i in range(amount):
        yield UserInfo(name=names[i], email=emails[i], password=passwords[i])