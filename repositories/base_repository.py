from database.connection import get_connection


class BaseRepository:

    def _get_connection(self):

        return get_connection()

    def _close(
            self,
            connection,
            cursor
    ):

        cursor.close()
        connection.close()

