class FieldFilterService(object):
    def __init__(self):
        pass

    def filter_contacts(self, filter):
        from services.contact_management_service import ContactManagementService
        contacts = ContactManagementService().get_all_contacts()
        results = set()
        for contact in contacts:
            for field in filter:
                if field == "first_name":
                    if contact.get_first_name() == filter[field]:
                        results.add(contact)
                elif field == "last_name":
                    if contact.get_last_name() == filter[field]:
                        results.add(contact)
                elif field == "phone":
                    if contact.get_phone() == filter[field]:
                        results.add(contact)
        formatted_results = []
        for item in results:
            formatted_results.append(ContactManagementService().format_contact_details(item))
        print(f"Found {len(formatted_results)} contact(s).")
        return formatted_results
