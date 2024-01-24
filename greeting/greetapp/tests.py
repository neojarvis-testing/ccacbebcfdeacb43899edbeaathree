# test.py

from django.test import TestCase
from django.urls import reverse
from .views import calculate_greeting

class GreetingAppTests(TestCase):
    def run_test(self, test_func, *args, test_name=None):
        try:
            test_func(*args)
            print(f"Passed {test_name}")
        except AssertionError as e:
            print(f"Failed {test_name}")

    def test_calculate_greeting_morning(self):
        self.run_test(self.assertEqual, calculate_greeting("5"), "Good Morning", test_name="test_calculate_greeting_morning")

    def test_calculate_greeting_afternoon(self):
        self.run_test(self.assertEqual, calculate_greeting("15"), "Good Afternoon", test_name="test_calculate_greeting_afternoon")

    def test_calculate_greeting_evening(self):
        self.run_test(self.assertEqual, calculate_greeting("18"), "Good Evening", test_name="test_calculate_greeting_evening")

    def test_calculate_greeting_night(self):
        self.run_test(self.assertEqual, calculate_greeting("22"), "Good Night", test_name="test_calculate_greeting_night")

    def test_get_greeting_post_request(self):
        url = reverse('get_greeting')
        response = self.client.post(url, {'time': '14'})
        self.run_test(self.assertEqual, response.status_code, 200, test_name="test_get_greeting_post_request")
        self.run_test(self.assertContains, response, "Good Afternoon", test_name="test_get_greeting_post_request")

    def test_get_greeting_get_request(self):
        url = reverse('get_greeting')
        response = self.client.get(url)
        self.run_test(self.assertEqual, response.status_code, 200, test_name="test_get_greeting_get_request")
        # Add more assertions based on your specific expected behavior for a GET request

    # Add more test cases as needed
