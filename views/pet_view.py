class PetView:

    def get_pet_data(self):

        name = input("Pet name: ")
        species = input("Species: ")
        age = int(input("Age: "))
        owner_id = int(input("Owner ID: "))

        return (
            name,
            species,
            age,
            owner_id
        )

    def get_pet_update_data(self):

        pet_id = int(
            input("Pet ID: ")
        )

        name = input(
            "New name: "
        )

        species = input(
            "New species: "
        )

        age = int(
            input("New age: ")
        )

        return (
            pet_id,
            name,
            species,
            age
        )

    def get_pet_id(self):

        return int(
            input("Pet ID: ")
        )

    def display_pets(
        self,
        pets
    ):

        print("\n--- PET LIST ---")

        for pet in pets:

            print(f"""
ID: {pet.id}
Name: {pet.name}
Species: {pet.species}
Age: {pet.age}
Owner ID: {pet.owner_id}
""")