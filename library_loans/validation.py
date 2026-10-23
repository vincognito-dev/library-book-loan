"""Validation helpers for library loans.

Each function returns normally if the input is valid,
or raises ValueError with a clear message if it is not.
None of them change any data.
"""
# ---------- Constants ----------
VALID_BOOK_TYPES = ("novel", "textbook", "reference")
LOAN_ID_PREFIX = "L"
MEMBER_ID_PREFIX = "M"
LOAN_ID_DIGIT_COUNT = 3
ASCII_DIGITS = "0123456789"
VALID_STATUSES = ("requested", "approved", "checked_out", "returned")

# ---------- Member ID ----------
def validate_member_id(member_id):
    if not isinstance (member_id, str):
        raise ValueError("Member ID must be a string")
    if member_id.strip() == "":
        raise ValueError("Member ID must not be blank")
    if not member_id.startswith(MEMBER_ID_PREFIX):
        raise ValueError("Member ID must start with the correct prefix")


# ---------- Book type ----------
def validate_book_type(book_type):
    if not isinstance (book_type, str):
        raise ValueError("Book Type must be a string")
    if book_type not in VALID_BOOK_TYPES:
        raise ValueError("Invalid Book Type")

    
# ---------- Loan ID ----------
def validate_loan_id(loan_id):
    if not isinstance (loan_id, str):
        raise ValueError("Loan ID must be a string")
    if not loan_id.startswith(LOAN_ID_PREFIX):
        raise ValueError("Loan ID must start with the right prefix")
    digits = loan_id[len(LOAN_ID_PREFIX):]
    if digits == "":
        raise ValueError("Loan ID must have digits after the prefix")
    if not all(c in ASCII_DIGITS for c in digits):
        raise ValueError("Loan ID must contain only digits 0-9 after the prefix")


# ---------- Librarian (approver) ----------
def validate_librarian(approved_by):
    if not isinstance (approved_by, str):
        raise ValueError("Approver must be a string")
    if approved_by.strip() == "":
        raise ValueError("Approver must not be blank")


# ---------- Status ----------
def validate_status(status):
    if not isinstance(status, str):
        raise ValueError("Status must be a string")
    if status not in VALID_STATUSES:
        raise ValueError("Invalid status")


