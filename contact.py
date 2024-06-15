 class ContactBook:
    def _init_(self):
        self.contacts = {}  # Initialize an empty dictionary to store contacts

    def add_contact(self):
        """Add a new contact to the book."""
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")
        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact '{name}' added successfully!")

    def view_contact(self):
        """View details of a specific contact."""
        name = input("Enter contact name to view details: ")
        if name in self.contacts:
            contact_info = self.contacts[name]
            print(f"Contact Details for '{name}':")
            print(f"Phone: {contact_info['phone']}")
            print(f"Email: {contact_info['email']}")
            print(f"Address: {contact_info['address']}")
        else:
            print(f"Contact '{name}' not found.")

    def update_contact(self):
        """Update contact information."""
        name = input("Enter contact name to update: ")
        if name in self.contacts:
            contact_info = self.contacts[name]
            phone = input("Enter new phone number (leave blank to keep existing): ")
            email = input("Enter new email address (leave blank to keep existing): ")
            address = input("Enter new address (leave blank to keep existing): ")
            if phone:
                contact_info['phone'] = phone
            if email:
                contact_info['email'] = email
            if address:
                contact_info['address'] = address
            print(f"Contact '{name}' updated successfully!")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self):
        """Delete a contact."""
        name = input("Enter contact name to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found.")


# Example usage
if _name_ == "_main_":
    my_contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            my_contact_book.add_contact()
        elif choice == '2':
            my_contact_book.view_contact()
        elif choice == '3':
            my_contact_book.update_contact()
        elif choice == '4':
            my_contact_book.delete_contact()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
