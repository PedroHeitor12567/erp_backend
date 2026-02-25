from enum import Enum

class Role(Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    SELLER = "seller"

    @classmethod
    def from_string(cls, value: str):
        try:
            return cls(value.lower())
        except ValueError:
            raise ValueError(f"Role inválida: {value}")
