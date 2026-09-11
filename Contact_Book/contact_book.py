# Dictionary to store contact names and phone numbers

contacts = {
  "Chika": "08012345678",
  "Ada": "09098765432",
  "Bryan": "08123456789"
}

# Add a new contact to the contact book

def add_contact():
  name= input("Enter a name: ").strip()
  number = input("Enter a phone number: ").strip()

  if not name:     # Validate that the name and phone number is not empty
    print("Name cannot be empty")
  elif not number:
    print("Phone number cannot be empty")

  elif any(key.lower() == name.lower() for key in contacts): # Check if the contact already exists (case-insensitive)
    print("Contact already exists")
  else:
    contacts[name] = number
    print("Contact Added")

# Display all saved contacts in the contact book
def view_contacts():
  if not contacts:
    print("No contacts found.")
  else:
    for key, value in contacts.items():
      print(f"{key}: {value}")

# Search for a contact by name in the contact book
def search_contact():
  search_name = input("Enter the name to search: ").strip()
  if not search_name:
    print("Search name cannot be empty")
    return
  
  for key, value in contacts.items(): # Check if the contact exists (case-insensitive)
    if key.lower() == search_name.lower():
      print(f"{key}'s phone number is {value}")
      return
  
  print("Contact not found")

# Delete a contact by name from the contact book
def delete_contact():
  delete_name = input("Enter the name of the contact to delete: ").strip()
  if not delete_name:
    print("Delete name cannot be empty")
    return
  for key in list(contacts.keys()):
    if key.lower() == delete_name.lower():
      del contacts[key]
      print(f"{key}'s contact has been deleted.")
      return
  
  print("Contact not found")


# Main loop to display the menu and handle user input
while True:
  print("\n---  CONTACT BOOK ---")
  menu = ["Add contact", "View Contacts", "Search contact", "Delete contact", "Exit"]

  # Display the menu options with corresponding numbers
  for index, value in enumerate(menu, start = 1):
    print(index, value)

# Make sure the user enters a valid number for the menu choice
  try:
      choice = int(input("choose an option(1-5) from the menu: "))
  except ValueError:
      print("Pls enter a valid number")
      continue

# Call the appropriate function based on the user's choice
  if choice == 1:
    add_contact()

  elif choice == 2:
    view_contacts()

  elif choice == 3:
    search_contact()

  elif choice == 4:
    delete_contact()

  elif choice == 5:
    print("Exiting...")
    break

  else:
    print("Invalid choice. Please select a valid option.")

