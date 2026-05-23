class Pet:
    def __init__(
            self,
            name,
            species,
            age,
            owner_id,
            pet_id=None
    ):
        self.id = pet_id
        self.name = name
        self.species = species
        self.age = age
        self.owner_id = owner_id


