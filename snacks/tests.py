from django.test import TestCase
from django.urls import reverse
from snacks.models import Snack
from django.contrib.auth import get_user_model

class ThingsTests(TestCase):
    def test_home_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_templete(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_snack_string_representation(self):
        snack = Snack.objects.create(
            name = "cupcake",
            purchaser = get_user_model().objects.create_user(
                username="tester",
                email="tester@email.com",
                password="pass"),
        description="Vanilla cupcake")
        self.assertEqual(str(snack), "cupcake")