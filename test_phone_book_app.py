import unittest
from phone_book_app import PhoneBook

class PhoneBookTestCases(unittest.TestCase):
	def test_create_contact(self):
		phonebook = PhoneBook()
		response = phonebook.create_contact("Doe","070000000")
		assert(response,"Contact created Successfully")

	def test_update_contact(self):
		phonebook = PhoneBook()
		response = phonebook.update_contact("Doe","070000000")
		assert(response,"Contact updated Successfully")

	def test_read_contact(self):
		phonebook = PhoneBook()
		response = phonebook.read_contact("Doe")
		assert(response,contacts["Doe"])

	def test_delete_contact(self):
		phonebook = PhoneBook()
		response = phonebook.delete_contact("Doe")
		assert(response,"Contact deleted Successfully")