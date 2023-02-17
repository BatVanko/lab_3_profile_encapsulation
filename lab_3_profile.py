class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {len(self.password)* "*"}'

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 > len(value) or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    def __has_atleast_8_char(self):
        return len(str(self.password)) > 8

    def __has_at_least_one_upper_case(self):
        return any([x.isupper() for x in str(self.password)])

    def __has_at_least_one_digit(self):
        return any([x.isdigit() for x in str(self.password)])

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        has_atleast_8_char = True
        if len(value) < 8 :
            has_atleast_8_char = False
        has_at_least_one_upper_case = any([x.isupper() for x in str(value)])
        has_at_least_one_digit = any([x.isdigit() for x in str(value)])

        if has_atleast_8_char and  has_at_least_one_upper_case and has_at_least_one_digit:
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")


# pesho = Profile('Pesho', '12345')
# pesho.username = 'Ivanov'
# print(pesho.username)
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)

# profile_with_invalid_password = Profile('My_username', 'My-password')
profile_with_invalid_username = Profile('Too_long_username', 'Any')