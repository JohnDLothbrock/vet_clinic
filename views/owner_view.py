class OwnerView:

    def get_owner_data(self):

        name = input("Owner name: ")
        phone = input("Phone: ")

        return name, phone

    def display_owners(self, owners):
        print("\n--- OWNER LIST ---")

        for owner in owners:
            print(f"""
    ID: {owner.id}
    Name: {owner.name}
    Phone: {owner.phone}
            """)

    def get_owner_update_data(self):
        owner_id = int(input("Owner ID: "))
        name = input("New name: ")
        phone = input("New phone: ")

        return owner_id, name, phone

    def get_owner_id(self):
        return int(input("Owner ID: "))