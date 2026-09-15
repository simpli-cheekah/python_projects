import json

# Try to load existing books from the JSON file
try:
  with open("books.json", "r") as file:
    books = json.load(file)
# If the file doesn't exist yet, start with an empty library
except FileNotFoundError:
    books = []

# Save the current books list to the JSON file
def save_books():
  with open("books.json", "w") as file:
    json.dump(books, file, indent = 4)


# Add a new book to the library
def add_book():
  title = input("What's the name of the book: ").strip()
  author = input("Who's the author of the book: ").strip()

  # Don't allow empty book titles or author names
  if not title or not author:
    print("Name and author of the book cannot be blank")
    return

  # Create a dictionary representing the new book  
  book = {
    "title": title,
    "author": author,
    "borrowed": False
  }

# Add the book to our list and save the updated list
  books.append(book)
  save_books()

  print(f"{title} added successfully")


# Display all books in the library
def view_books():
  if not books:   
    print("No books in the library.")
    return
  else:
    print("\n--- Books ---")
    for book in books:
      print(f"Title: {book['title']}\nAuthor: {book['author']}")

      # Show whether the book is borrowed or available
      if book["borrowed"]:
       print("Status: Borrowed")

      else:
        print("Status: Available")
    

# Search for a book by it's title
def search_book():
  search_name = input("Enter the name to search: ").strip()
  if not search_name:
    print("Search name cannot be empty")
    return

  # Loop through every book and compare titles
  for book in books: 
    if book["title"].lower() == search_name.lower():  # Check if the book exists (case-insensitive)
      print(f"Title: {book['title']}\nAuthor: {book['author']}")
      if book["borrowed"]:
        print("Status: Borrowed")
      else:
        print("Status: Available")
      break

  # This runs if the loop finishes without finding a match
  else:
      print("Book not found")


# Borrow a book
def borrow_book():
  borrow_name = input("Enter the name of the book to borrow: ").strip()
  if not borrow_name:
    print("Search name cannot be empty")
    return
  for book in books:
    if book["title"].lower() == borrow_name.lower():   # Find the book, ignoring uppercase/lowercase differences

      if book["borrowed"]:      # Don't allow someone to borrow an already borrowed book
        print("This book is already borrowed")
        break
      # Mark the book as borrowed
      else:
        book["borrowed"]= True
        save_books()
        print("This book was borrowed")
        break
  else:
    print("Book not found")


# Return a borrowed book
def return_book():
  return_name = input("Enter the name of the book to return: ").strip()
  if not return_name:
    print("Search name cannot be empty")
    return
  for book in books:
    if book["title"].lower() == return_name.lower():
      if not book["borrowed"]:   # Don't return a book that isn't borrowed
        print("This book is currently not borrowed")
        break
      else:
        book["borrowed"]= False   # Mark the book as available again
        save_books()
        print("This book was returned")
        break
  else:
    print("Book not found")


# Delete a book from the library
def delete_book():
  delete_name = input("Enter the name of the book to delete: ").strip()
  if not delete_name:
    print("Delete name cannot be empty")
    return
  
  for book in books:
    if book["title"].lower() == delete_name.lower():  # Find the book, ignoring uppercase/lowercase differences

      books.remove(book)   # Remove the matching book from the books list

      save_books()  # Save the updated list so the deletion persists

      print(f"{book['title']} was deleted successfully.")
      break
  else:
    print("book not found")


# Main program loop
while True:
  # Display the available actions
  menu = ["Add book", "View books", "Search book", "Borrow book", "Return book", "Delete book", "Exit"]

  print("\n --- LIBRARY MANAGER ---")
  for index, value in enumerate(menu, start = 1):
    print(index, value)
  # Make sure the user enters a number
  try:
    choice = int(input("choose an option(1-7) from the menu: "))
  except ValueError:
    print("Pls enter a valid number")
    continue

  # Perform the action selected by the user
  if choice == 1:
    add_book()

  elif choice == 2:
    view_books()

  elif choice == 3:
    search_book()

  elif choice == 4:
    borrow_book()

  elif choice == 5:
    return_book()

  elif choice == 6:
    delete_book()

  elif choice == 7:
    print("Exiting...")
    break

  else:
    print("Invalid choice. Please select a valid option.")
