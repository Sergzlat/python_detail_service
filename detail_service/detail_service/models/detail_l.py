from enum import Enum
from datetime import datetime

class UserType(Enum):
    Unknown = 0
    Nextdetail = 1
    DetailL = 2
    Admin = 3

class Entity:
    def __init__(self):
        self.id = None
        self.is_deleted = False

class DetailL(Entity):
    def __init__(self):
        super().__init__()
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.birth_date = datetime.min
        self.email = None
