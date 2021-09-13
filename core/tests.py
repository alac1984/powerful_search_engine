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