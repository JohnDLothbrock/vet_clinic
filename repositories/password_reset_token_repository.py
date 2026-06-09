from database.connection import get_connection

from models.password_reset_token import (
    PasswordResetToken
)


class PasswordResetTokenRepository:

    def create(
            self,
            password_reset_token: PasswordResetToken
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            INSERT INTO PasswordResetTokens (
                user_id,
                token_hash,
                expires_at,
                used,
                created_at
            )
            OUTPUT INSERTED.id
            VALUES (?, ?, ?, 0, SYSDATETIME())
            """

            cursor.execute(
                query,
                (
                    password_reset_token.user_id,
                    password_reset_token.token_hash,
                    password_reset_token.expires_at
                )
            )

            row = cursor.fetchone()

            connection.commit()

            return row[0]

        finally:

            cursor.close()
            connection.close()

    def get_valid_by_token_hash(
            self,
            token_hash
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                id,
                user_id,
                token_hash,
                expires_at,
                used,
                created_at,
                used_at
            FROM PasswordResetTokens
            WHERE token_hash = ?
            AND used = 0
            AND expires_at > SYSDATETIME()
            """

            cursor.execute(
                query,
                (
                    token_hash,
                )
            )

            row = cursor.fetchone()

            if not row:

                return None

            return PasswordResetToken(
                password_reset_token_id=row.id,
                user_id=row.user_id,
                token_hash=row.token_hash,
                expires_at=row.expires_at,
                used=row.used,
                created_at=row.created_at,
                used_at=row.used_at
            )

        finally:

            cursor.close()
            connection.close()

    def mark_as_used(
            self,
            password_reset_token_id
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            UPDATE PasswordResetTokens
            SET
                used = 1,
                used_at = SYSDATETIME()
            WHERE id = ?
            """

            cursor.execute(
                query,
                (
                    password_reset_token_id,
                )
            )

            connection.commit()

        finally:

            cursor.close()
            connection.close()

    def expire_active_tokens_for_user(
            self,
            user_id
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            UPDATE PasswordResetTokens
            SET
                used = 1,
                used_at = SYSDATETIME()
            WHERE user_id = ?
            AND used = 0
            """

            cursor.execute(
                query,
                (
                    user_id,
                )
            )

            connection.commit()

        finally:

            cursor.close()
            connection.close()