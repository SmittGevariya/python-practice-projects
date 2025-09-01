contacts = {
    "contacts": [
        {
            "name": "Smit",
            "phone": ["12345", "67890"],
            "email": "smit@example.com",
            "address": {"city": "Ahmedabad", "zip": "382345"}
        },
        {
            "name": "yash",
            "phone": ["989898"],
            "email": "yash@example.com",
            "address": {"city": "Surat", "zip": "382350"}
        }
    ]
}

def display_contacts(contact_list):
    for contact in contact_list["contacts"]:
        print(f"Name   : {contact['name']}")
        print(f"Phones : {', '.join(contact['phone'])}")
        print(f"Email  : {contact['email']}")
        print(f"City   : {contact['address']['city']}")
        print(f"Zip    : {contact['address']['zip']}")
        print("-" * 40)

display_contacts(contacts)
