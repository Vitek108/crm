from django.test import TestCase
from django.shortcuts import reverse


class HomePageTest(TestCase):

    def test_get(self):  # název metody s "test" na začátku djangu značí, že zde má vykonat jednotlivý test
        response = self.client.get(reverse("landing-page")) # client = způsob poslání requestu (jako request), reverse - místo tvrdého url dám jen název path
        self.assertEqual(response.status_code, 200) # test porovná status kód s hodnotou 200 a pokud neodpovídá, hodí chybu
        self.assertTemplateUsed(response, template_name="landing.html")
