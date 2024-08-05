```markdown
# Library Management 

This Python project is designed to manage a library using a MySQL database. It includes various entities such as `Supplier`, `Book Genre`, `Author`, `Book`, `Member`, and `Loan`. The application uses the `customtkinter` and `tkinter` packages for the graphical user interface.

## Features

- **CRUD for Suppliers**: Add, edit, delete, and display suppliers.
- **CRUD for Book Genres**: Add, edit, delete, and display book genres.
- **CRUD for Authors**: Add, edit, delete, and display authors.
- **CRUD for Books**: Add, edit, delete, and display books.
- **CRUD for Members**: Add, edit, delete, and display members.
- **Loan a Book**: Associate a book with a member through a loan process.

## Prerequisites

- Python 3.8 or higher
- MySQL database
- `customtkinter` and `tkinter` packages

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/SaadiaEl08/library-management.git
   cd library-management
   ```

2. Install the required Python packages:

   ```bash
   pip install customtkinter mysql-connector-python
   ```

## Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. Use the graphical user interface to manage suppliers, book genres, authors, books, members, and loans .
   - username:worker
   - password:work1234

## Project Structure

- **main.py**: The main entry point of the application.
- **model/**: Contains the classes for the various entities (Supplier, Book Genre, Author, Book, Member, Loan).
- **view/**: Contains the GUI code using `customtkinter` and `tkinter`.
- **controller/**: Manage the relation between the views and models.



---

This project is part of an educational program to help you learn to work with Python, MySQL, and GUI development using `customtkinter` and `tkinter`. Have fun and happy coding!
```