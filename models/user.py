class User:

    def __init__(
            self,
            username,
            email,
            password_hash,
            role_id,
            active,
            user_id=None
    ):

        self.id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role_id = role_id
        self.active = active