from models.models import User, user_schema
from responses import fail_responses

class UserCrud:
    def read_one_user(email: str):
        """Reads one user, selected by email"""
        user = User.query.filter(User.email == email).first()

        if user:
                return user_schema.dump(user)
        else:
            return fail_responses.user_not_found(email)