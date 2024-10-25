# Simple Contact Manager (OOP-Based App to Store Contacts)

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def get_info(self):
        return f"{self.name}: {self.phone}, {self.email}"

class ContactManager:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def view_contacts(self):
        for contact in self.contacts:
            print(contact.get_info())

# Create the contact manager
manager = ContactManager()
 
# Create contacts
contact1 = Contact("Alice", "123-456-7890", "alice@example.com")
contact2 = Contact("Bob", "987-654-3210", "bob@example.com")
 
# Add contacts to the manager
manager.add_contact(contact1)
manager.add_contact(contact2)
 
# View all contacts
manager.view_contacts()
