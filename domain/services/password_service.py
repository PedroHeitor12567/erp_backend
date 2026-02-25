from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class PasswordService:
    @staticmethod
    def hash_password(password: str) -> str:
        if len(password) < 6:
            raise ValueError("Senha deve ter no mínimo 6 caracteres")
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)