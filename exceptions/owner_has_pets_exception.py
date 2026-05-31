class OwnerHasPetsException(
    Exception
):

    def __init__(
            self,
            owner_id
    ):

        super().__init__(
            f"Owner ID {owner_id} still has pets assigned."
        )

