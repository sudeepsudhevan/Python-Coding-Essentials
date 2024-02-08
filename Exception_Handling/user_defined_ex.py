class InvalidPasswordError(Exception):
    def __init__(self, password, message="Invalid password"):
        self.password = password
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.password} -> {self.message}"


def check_password(password):
    # check if the password is at least 8 characters long
    if len(password) < 8:
        raise InvalidPasswordError(
            password, "Password must be at least 8 characters long"
        )
    # check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        raise InvalidPasswordError(password, "Password must contain at least one digit")
    # check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        raise InvalidPasswordError(
            password, "Password must contain at least one uppercase letter"
        )
    # if all checks pass, return True
    return True


try:
    password = input("Enter a password: ")
    if check_password(password):
        print("Password is valid")
except InvalidPasswordError as e:
    print(e)
