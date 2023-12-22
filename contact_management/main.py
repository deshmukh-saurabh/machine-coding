from services.contact_management_service import ContactManagementService
from models.contact import Contact

cms = ContactManagementService()
cms.add_contact(Contact(1, "Bob", "Doe", "1234567890"))
cms.print_all_contacts()
cms.add_contact(Contact(2, "Bill", "Smith", "9876543210"))
cms.print_all_contacts()
cms.add_contact(Contact(3, "Ally", "Morgan", "8765490870"))
cms.print_all_contacts()
cms.update_contact(3, {"phone": "9876512340"})
cms.print_all_contacts()
cms.add_contact(Contact(4, "Milly", "Bond", "6754837560"))
cms.print_all_contacts()
print(cms.search_contacts("B", filter_type="string_filter"))
print(cms.search_contacts("Al", filter_type="string_filter"))
print(cms.search_contacts("bob", filter_type="string_filter"))
print(cms.search_contacts({"first_name": "Bob"}, filter_type="field_filter"))
print(cms.search_contacts({"last_name": "ally"}, filter_type="field_filter"))
print(cms.search_contacts({"phone": "9876543210"}, filter_type="field_filter"))