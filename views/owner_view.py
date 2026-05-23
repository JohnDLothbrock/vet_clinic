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
