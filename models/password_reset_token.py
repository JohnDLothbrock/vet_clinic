class PasswordResetToken:

    def __init__(
            self,
            user_id,
            token_hash,
            expires_at,
            used=False,
            created_at=None,
            used_at=None,
            password_reset_token_id=None
    ):

        self.id = password_reset_token_id
        self.user_id = user_id
        self.token_hash = token_hash
        self.expires_at = expires_at
        self.used = used
        self.created_at = created_at
        self.used_at = used_at