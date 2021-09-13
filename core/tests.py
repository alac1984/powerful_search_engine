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

    # If user type something and database didn't find results
    # show a message informing that to the user

    # If a user try to access search/ endpoint with a get request
    # redirect it to index page

    # If a user type something and database find results,
    # show then to the user (inspect if it has options)

