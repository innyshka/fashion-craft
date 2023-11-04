from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", password="admin"
        )
        self.client.force_login(self.admin_user)
        self.designer = get_user_model().objects.create_user(
            username="designer", password="testdesigner", pseudonym="designer"
        )

    def test_designer_pseudonym_listed(self) -> None:
        """Test that pseudonym is in list_display on designer page"""
        url = reverse("admin:catalog_designer_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.designer.pseudonym)

    def test_designer_detail_pseudonym_listed(self) -> None:
        """Test that pseudonym is on designer detail admin page"""
        url = reverse("admin:catalog_designer_change", args=[self.designer.id])
        res = self.client.get(url)

        self.assertContains(res, self.designer.pseudonym)
