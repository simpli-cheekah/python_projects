print("Welcome to chika bank")

# Keep the balance outside the while loop so that it is not reset to 1000 every time the loop runs
balance = 1000  # starting balance
print(f"Your balance is: {balance}")

while True:
  # Display the bank menu
  print("\n---  CHIKA BANK MENU ---")
  menu = ["Deposit", "Withdraw", "Pay bill", "Check balance", "Exit"]

  # Number each menu option starting from 1 and display it
  for index, items in enumerate(menu, start=1):
    print(index, items)

  # Get and validate the user's menu choice
  try:
    choice = int(input("choose an option(1-5) from the menu: "))
  except ValueError:
    print("Pls enter a valid number")
    continue

  # Depending on the user's choice, perform the corresponding action

  if choice == 1:
    try:
      deposit = int(input("How much do you want to deposit? "))
    except ValueError:
      print("Pls enter a valid number")
      continue
    #Reject zero and negative numbers for deposit
    if deposit <= 0:
      print("Zero and negative numbers are invalid")
    else:
      balance += deposit
    print("Deposit successful")
    print(f"Your new balance is: {balance}")

  elif choice == 2:
    try:
      withdraw = int(input("How much do you want to withdraw? "))
    except ValueError:
      print("Pls enter a valid number")
      continue
    if withdraw <= 0:
      print("Zero and negative numbers are invalid")
    # Only allow withdrawal if the account has sufficient funds
    elif withdraw <= balance:
      print("Withdrawal successful")
      balance -= withdraw
    else:
      print("Insufficient balance")
    print(f"Your new balance is: {balance}")
      
  elif choice == 3:
    try:
      bill = int(input("How much is your bill? "))
    except ValueError:
      print("Pls enter a valid number")
      continue
    if bill <= 0:
      print("Zero and negative numbers are invalid")
    elif bill <= balance:
      balance -= bill
    else:
      print("Insufficient balance")
    print(f"Your new balance is: {balance}")

  elif choice == 4:
    print(f"Your current balance is: {balance}")

# Exit the while loop and end the program if the user chooses to exit
  elif choice == 5:
    print("Goodbye")
    break

  else:
    print("Your option is invalid")

      
