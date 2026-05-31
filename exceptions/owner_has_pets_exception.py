from exceptions.application_exception import (
    ApplicationException
)


class OwnerHasPetsException(
    ApplicationException
):

    def __init__(
            self,
            owner_id
    ):

        super().__init__(
            message=(
                f"Owner ID {owner_id} "
                f"still has pets assigned."
            ),
            status_code=400
        )