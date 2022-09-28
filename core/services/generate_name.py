from faker import Faker

fake = Faker()


# Generate name of user
def generate_name() -> str:
    return str(fake.first_name())
