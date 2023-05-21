from base_model import BaseModel

class User:
    def __init__(self, user_id, name, email, password, phone):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
