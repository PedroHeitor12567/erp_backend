from uuid import UUID, uuid4
from datetime import datetime

from domain.value_objects.email import Email
from domain.value_objects.role import Role


class User:

    def __init__(self, id: UUID | None, name:str, email: Email, password_hash: str, role: Role, created_at: datetime | None = None):
        self.id = id or uuid4()
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.created_at = created_at or datetime.utcnow()
        self._is_active = True

    @property
    def is_active(self) -> bool:
        return self._is_active

    def activate(self):
        self._is_active = True

    def deactivate(self):
        self._is_active = False

    def is_admin(self) -> bool:
        return self.role == Role.ADMIN

    def can_manage_users(self) -> bool:
        return self.role in [Role.ADMIN, Role.MANAGER]

    def update_name(self, new_name: str):
        if not new_name or len(new_name.strip()) < 3:
            raise ValueError("Nome deve ter no mínimo 3 caracteres")
        self.name = new_name.strip()

    def update_role(self, new_role: Role):
        self.role = new_role