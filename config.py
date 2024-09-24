
class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    INGREDIENTS_PATH = '/api/ingredients'
    ORDERS_PATH = '/api/orders'
    CREATE_USER_PATH = '/api/auth/register'
    DELETE_USER_PATH = '/api/auth/user'
    AUTH_PATH = '/api/auth/login'
    GET_USER_INFO_PATH = '/api/auth/user'
    EDIT_USER_INFO_PATH = '/api/auth/user'


class ResponseMessages:

    USER_ALREADY_EXISTS_ERROR_TEXT = 'User already exists'
    MISSING_REQUIRED_FILED_ERROR_TEXT = 'Email, password and name are required fields'
    INCORRECT_EMAIL_OR_PASSWORD_ERROR_TEXT = 'email or password are incorrect'
    SHOULD_BE_AUTHORIZED_TO_EDIT_USER_INFO_ERROR_TEXT = 'You should be authorised'