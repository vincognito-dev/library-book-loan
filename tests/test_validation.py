"""Tests for library_loans/validation.py."""

import unittest

from library_loans.validation import (
    validate_member_id,
    validate_book_type,
    validate_loan_id,
    validate_librarian,
    validate_status,
)


class TestMemberId(unittest.TestCase):

    def test_valid_member_id_passes(self):
        validate_member_id("M001")

    def test_blank_member_id_rejected(self):
        with self.assertRaises(ValueError):
            validate_member_id("   ")

    def test_empty_member_id_rejected(self):
        with self.assertRaises(ValueError):
            validate_member_id("")

    def test_none_member_id_rejected(self):
        with self.assertRaises(ValueError):
            validate_member_id(None)

    def test_number_member_id_rejected(self):
        with self.assertRaises(ValueError):
            validate_member_id(123)

    def test_wrong_prefix_member_id_rejected(self):
        with self.assertRaises(ValueError):
            validate_member_id("X001")


class TestBookType(unittest.TestCase):

    def test_valid_book_types_pass(self):
        for book_type in ("novel", "textbook", "reference"):
            validate_book_type(book_type)

    def test_unknown_book_type_rejected(self):
        with self.assertRaises(ValueError):
            validate_book_type("comic")

    def test_capitalised_book_type_rejected(self):
        with self.assertRaises(ValueError):
            validate_book_type("Novel")

    def test_none_book_type_rejected(self):
        with self.assertRaises(ValueError):
            validate_book_type(None)

class TestLoanId(unittest.TestCase):

    def test_valid_loan_id_passes(self):
        validate_loan_id("L001")

    def test_large_loan_id_passes(self):
        validate_loan_id("L1000")
    
    def test_loan_id_with_no_digits_rejected(self):
        with self.assertRaises(ValueError):
            validate_loan_id("L")

    def test_lowercase_prefix_rejected(self):
        with self.assertRaises(ValueError):
            validate_loan_id("l001")

    def test_missing_prefix_rejected(self):
        with self.assertRaises(ValueError):
            validate_loan_id("001")

    def test_fullwidth_digits_rejected(self):
        with self.assertRaises(ValueError):
            validate_loan_id("L O O 1 ")

    def test_space_inside_rejected(self):
        with self.assertRaises(ValueError):
            validate_loan_id("L 01")

    def test_none_loan_id_rejected(self):
        with self.assertRaises(ValueError):
            validate_loan_id(None)

    
class TestLibrarian(unittest.TestCase):

    def test_valid_librarian_passes(self):
        validate_librarian("LIB01")

    def test_blank_librarian_rejected(self):
        with self.assertRaises(ValueError):
            validate_librarian("   ")

    def test_none_librarian_rejected(self):
        with self.assertRaises(ValueError):
            validate_librarian(None)


class TestStatus(unittest.TestCase):

    def test_valid_statuses_pass(self):
        for status in ("requested", "approved", "checked_out", "returned"):
            validate_status(status)

    def test_unknown_status_rejected(self):
        with self.assertRaises(ValueError):
            validate_status("pending")

    def test_none_status_rejected(self):
        with self.assertRaises(ValueError):
            validate_status(None)


if __name__ == "__main__":
    unittest.main()