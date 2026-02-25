import re

class Email:
    def __init__(self, value: str):
        self.value = self._validate(value)

    def validate(self, email: str) -> str:
        email = email.strip().lower()
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(pattern, email):
            raise ValueError(f"E-mail inválido: {email}")

        return email

    def __str__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, Email):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)