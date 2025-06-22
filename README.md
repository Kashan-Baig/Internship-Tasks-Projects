# 📚 Python Utilities – Contact Book & Grade Book

A collection of beginner-friendly **Python CLI applications** to manage everyday data — one for storing **contacts** and the other for managing **student grades**. Simple, useful, and perfect for learning **file handling**, **data validation**, and **MySQL integration**.

---

## 📒 Contact Book

Manage contacts with name, phone number, and email — all saved in a `contacts.json` file.

### 🔹 Features
- ➕ Add new contacts with validation
- 🔍 Search contacts by phone number
- 📄 View all saved contacts
- 💾 Data stored in JSON (readable + editable)
- ✅ Validates:
  - Phone number must be **11 digits**
  - Email must follow standard format

### 📂 Tech Used
- Python `json` and `re` libraries (no external packages)

---

## 📝 Grade Book

A command-line grade manager connected to a **MySQL** database.

### 🔹 Features
- ➕ Add student grades
- 🖊️ Update grades by ID
- 🗑️ Delete student records
- 📊 View all records
- 📈 Calculate average, highest marks, etc.

### 📂 Tech Used
- Python with `mysql-connector-python`
- MySQL database (custom schema)

---

## 🚀 Getting Started

1. Clone the repo or download the files.
2. Run the script from terminal:
   ```bash
   python contact_book.py      # For Contact Book
   python grade_book.py        # For Grade Book
