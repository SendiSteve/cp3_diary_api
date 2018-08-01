import json
import unittest
from tests.base import BaseTestCase


class EntriesTestCase(BaseTestCase):

    # @unittest.skip('checking')
    def test_user_creates_entry_successfully(self):
        with self.client:
            self.login_user("test@test.com", "password")
            response = self.create_entry(
                'Meeting with the CEO Twitter',
                'Discuss about new marketing strategies')
            result = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertEqual(result.get('message'),
                             'Entry recorded successfully.')
    
            res = self.create_entry(
                'Meeting with the CEO Twitter',
                'Discuss about new marketing strategies'
            )
            result1 = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 400)
            self.assertEqual(result1.get(
                'message'), 'Cannot have entries with the same title.')

    def test_entry_title_is_black(self):
        with self.client:
            self.login_user("test@test.com", "password")
            response = self.create_entry(
                '',
                'Discuss about new marketing strategies')
            result = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(result.get('message'),
                             'Please enter a valid entry.')

    def test_entry_notes_is_black_or_has_few_characters(self):
        with self.client:
            self.login_user("test@test.com", "password")
            response = self.create_entry(
                'Meeting with the Bootcamp fellows',
                'Dis')
            result = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(result.get('message'),
                             'Please enter notes with atleast 5 characters.')

    def test_retrieve_all_entries(self):
        """Test all entries can be retrieved successfully"""
        with self.client:
            # Create an entry first
            self.create_entry(
                "Meeting with CEO Andela",
                "Discuss about marketing strategies")

            # retrieve the created entry
            response = self.get_all_entries()

            # verify that the result is success with 200 status code
            self.assertEqual(response.status_code, 200)
    
    def test_user_has_no_entries(self):
        with self.client:
            response = self.get_all_entries()
            self.assertEqual(response.status_code, 200)
            result = json.loads(response.data.decode())
            self.assertTrue(result, None)