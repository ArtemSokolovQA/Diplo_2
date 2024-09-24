from faker import Faker

fake = Faker()

class UserData:

    registered_user_data = {
        "email": "ArtemSokoLoveTest@yandex.ru",
        "password": "fuuuuuu",
        "name": "brahiozavr"
}

    create_user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.user_name()
    }

    create_user_data_empty_required_field = {
        "email": fake.email(),
        "password": '',
        "name": fake.user_name()
    }