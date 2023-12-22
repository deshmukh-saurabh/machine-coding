import re


class StringFilterService(object):
    def __init__(self):
        pass

    def filter_contacts(self, filter):
        from services.contact_management_service import ContactManagementService
        contacts = ContactManagementService().get_all_contacts()
        results = set()
        for contact in contacts:
            if re.search(filter, contact.get_first_name(), re.IGNORECASE):
                results.add(contact)
            if re.search(filter, contact.get_last_name(), re.IGNORECASE):
                results.add(contact)
            if re.search(filter, contact.get_phone(), re.IGNORECASE):
                results.add(contact)

        formatted_results = []
        for item in results:
            formatted_results.append(ContactManagementService().format_contact_details(item))
        print(f"Found {len(formatted_results)} contact(s).")
        return formatted_results
