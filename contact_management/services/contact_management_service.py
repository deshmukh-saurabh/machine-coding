from models.filter import FilterFactory


class ContactManagementService(object):
    contacts = []

    def __init__(self):
        pass

    def format_contact_details(self, contact):
        return {"id": contact.get_id(), "first_name": contact.get_first_name(), "last_name": contact.get_last_name(), "phone": contact.get_phone()}

    def print_all_contacts(self):
        print("-" * 100)
        for contact in __class__.contacts:
            print(self.format_contact_details(contact))
        print("-" * 100)

    def get_all_contacts(self):
        return __class__.contacts

    def add_contact(self, contact):
        self.contacts.append(contact)

    def update_contact(self, id, updated_details):
        updated = False
        for contact in self.contacts:
            if contact.get_id() == id:
                for field in updated_details:
                    if field == "first_name":
                        contact.set_first_name(updated_details[field])
                    elif field == "last_name":
                        contact.set_last_name(updated_details[field])
                    elif field == "phone":
                        contact.set_phone(updated_details[field])
                updated = True
                print(f"Updated contact with id: {id}")
        if not updated:
            print(f"Could not find a contact with id: {id}")

    def search_contacts(self, filter, filter_type):
        return FilterFactory().get_filter(filter_type).apply_filter(filter)
