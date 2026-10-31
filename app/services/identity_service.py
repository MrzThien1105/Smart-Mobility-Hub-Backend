from app.models.entities import Role, StudentProfile, User, UserRole


class IdentityService:
    def __init__(self, uow):
        self.uow = uow

    def authenticate_sso(self, sso_subject: str) -> User:
        raise NotImplementedError

    def provision_user(self, identity_data: dict) -> User:
        raise NotImplementedError

    def get_user(self, user_id: str) -> User:
        raise NotImplementedError

    def update_user(self, user_id: str, changes: dict) -> User:
        raise NotImplementedError

    def assign_role(self, user_id: str, role_id: str) -> UserRole:
        raise NotImplementedError

    def revoke_role(self, user_id: str, role_id: str) -> None:
        raise NotImplementedError

    def authorize(self, user_id: str, permission: str) -> bool:
        raise NotImplementedError

    def create_student_profile(self, user_id: str, profile_data: dict) -> StudentProfile:
        raise NotImplementedError

    def suspend_user(self, user_id: str) -> User:
        raise NotImplementedError
