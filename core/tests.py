from django.test import TestCase
from django.urls import reverse, reverse_lazy


class SearchViewTests(TestCase):
    def test_method_get_redirect_to_index(self):
        """
        If the user tries to search without a query
        redirect it to index url
        """
        response = self.client.get(reverse('core:search'))
        self.assertEqual(response.status_code, 302)

    def test_search_without_results(self):
        """
        If the user's query do not retrieve anything
        show him a message informing that
        """
        response = self.client.get(reverse('core:search') + '?q=Angel')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response.content, "We didn\'t find anything on our database. We\'re sorry")

        # If a user type something and database find results,
        # show then to the user (inspect if it has options)

