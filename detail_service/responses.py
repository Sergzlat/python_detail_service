from dataclasses import dataclass

@dataclass
class DetailLResponse:
    id: int
    first_name: str
    middle_name: str
    last_name: str
    birth_date: str
    email: str
    is_deleted: bool
