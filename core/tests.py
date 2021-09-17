from django.test import TestCase
from django.urls import reverse


class SearchViewTests(TestCase):
    def test_no_query_search(self):
        """
        If the user do not input anything, show him a message
        informing he does not searched for anything
        """
        response = self.client.post(reverse('core:search'), {'query': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You didn&#x27;t search for anything")

    def test_method_get_redirect_to_index(self):
        """
        If the user tries to access search/ endpoint directly from the
        browser (with a GET request) redirect it to index url
        """
        response = self.client.get(reverse('core:search'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Powerful Search Engine')

    # If user type something and database didn't find results
    # show a message informing that to the user

    # If a user type something and database find results,
    # show then to the user (inspect if it has options)

