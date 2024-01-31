class DbTools:
    def __init__(self, user, password):
        self.USER = user
        self.PASSWORD = password

    def get_user(self):
        return self.USER

    def get_password(self):
        return self.PASSWORD
