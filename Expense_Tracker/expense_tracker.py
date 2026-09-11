expenses = []


def add_expense():
    # Get the expense details from the user and validate the input
    name = input("Enter the name of the expense: ").strip()

    try:
        amount = int(input("Enter the amount of the expense: ₦").strip())
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    # Make sure the amount is greater than zero
    if amount <= 0:
        print("Amount must be greater than zero.")
        return
        
    category = input("Enter the category of the expense: ").strip()

    # Make sure the name and category are not empty
    if not name or not category:
        print("Name and category cannot be empty.")
        return

    # Add the expense to the list of expenses
    expenses.append({"name": name, "amount": amount, "category": category})
    print(f"Expense '{name}' added successfully.")



 # Check if there are any expenses recorded
def view_expenses():
    if not expenses:   
        print("No expenses recorded.")
        return

    # Display all the expenses
    print("\n--- Expenses ---")
    for expense in expenses:
        print(f"Name: {expense['name']}, Amount: ₦{expense['amount']}, Category: {expense['category']}")

# Add the amount of all expenses and display the total
def calculate_total():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f" Total expenses: ₦{total:.2f}")


# Main loop to display the menu and handle user input
while True:
  print("\n---  EXPENSE TRACKER ---")
  menu = ["Add expense", "View expenses", "Calculate total", "Exit"]

  # Display the menu options with corresponding numbers
  for index, value in enumerate(menu, start = 1):
    print(index, value)

# Make sure the user enters a valid number for the menu choice
  try:
      choice = int(input("choose an option(1-4) from the menu: "))
  except ValueError:
      print("Pls enter a valid number")
      continue

# Call the appropriate function based on the user's choice
  if choice == 1:
    add_expense()

  elif choice == 2:
    view_expenses()

  elif choice == 3:
    calculate_total()

  elif choice == 4:
    print("Exiting...")
    break

  else:
    print("Invalid choice. Please select a valid option.")

