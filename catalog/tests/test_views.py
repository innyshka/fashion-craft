from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import Material, Size, ClothingType, Clothing, Designer

MATERIAL_LIST_URL = reverse("catalog:material-list")
SIZE_LIST_URL = reverse("catalog:size-list")
CLOTHING_TYPE_LIST_URL = reverse("catalog:clothing-type-list")
CLOTHING_LIST_URL = reverse("catalog:clothing-list")
DESIGNER_LIST_URL = reverse("catalog:designer-list")


class AccessControlTestTest(TestCase):
    def assert_access_control(self, url_name) -> None:
        res = self.client.get(url_name)
        self.assertNotEquals(res.status_code, 200)
        self.assertRedirects(res, f"/accounts/login/?next={url_name}")

    def test_material_login_required(self) -> None:
        self.assert_access_control(MATERIAL_LIST_URL)

    def test_size_login_required(self) -> None:
        self.assert_access_control(SIZE_LIST_URL)

    def test_clothing_type_login_required(self) -> None:
        self.assert_access_control(CLOTHING_TYPE_LIST_URL)

    def test_clothing_login_required(self) -> None:
        self.assert_access_control(CLOTHING_LIST_URL)

    def test_designer_login_required(self) -> None:
        self.assert_access_control(DESIGNER_LIST_URL)


class PrivateMaterialTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="testpass123",
            pseudonym="ABC123455",
        )
        for i in range(15):
            Material.objects.create(
                name=f"name_{i}",
            )
        self.client.force_login(self.user)

    def test_retrieve_material(self) -> None:
        response = self.client.get(MATERIAL_LIST_URL)
        self.assertEquals(response.status_code, 200)
        material = Material.objects.all()
        self.assertEquals(
            list(response.context["material_list"]),
            list(material)[:15],
        )
        self.assertTemplateUsed(response, "catalog/material_list.html")

    def test_search_material_by_name(self) -> None:
        searched_name = "name_8"
        response = self.client.get(MATERIAL_LIST_URL, {"name": searched_name})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.context["material_list"][0],
            Material.objects.get(name=searched_name),
        )


class PrivateSizeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="testpass123",
            pseudonym="ABC123455",
        )
        for i in range(15):
            Size.objects.create(name=f"name_{i}", description=f"test_{i}")
        self.client.force_login(self.user)

    def test_retrieve_size(self) -> None:
        response = self.client.get(SIZE_LIST_URL)
        self.assertEquals(response.status_code, 200)
        size = Size.objects.all()
        self.assertEquals(
            list(response.context["size_list"]),
            list(size)[:15],
        )
        self.assertTemplateUsed(response, "catalog/size_list.html")

    def test_search_size_by_name(self) -> None:
        searched_name = "name_8"
        response = self.client.get(SIZE_LIST_URL, {"name": searched_name})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.context["size_list"][0],
            Size.objects.get(name=searched_name),
        )


class PrivateClothingTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="testpass123",
            pseudonym="ABC123455",
        )
        for i in range(15):
            ClothingType.objects.create(
                name=f"name_{i}",
            )
        self.client.force_login(self.user)

    def test_retrieve_clothing_type(self) -> None:
        response = self.client.get(CLOTHING_TYPE_LIST_URL)
        self.assertEquals(response.status_code, 200)
        clothing_type = ClothingType.objects.all()
        self.assertEquals(
            list(response.context["clothing_type_list"]),
            list(clothing_type)[:15],
        )
        self.assertTemplateUsed(response, "catalog/clothingtype_list.html")

    def test_search_clothing_type_by_name(self) -> None:
        searched_name = "name_8"
        response = self.client.get(
            CLOTHING_TYPE_LIST_URL, {"name": searched_name}
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.context["clothing_type_list"][0],
            ClothingType.objects.get(name=searched_name),
        )


class PrivateClothingTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="testpass123",
            pseudonym="ABC123455",
        )
        for i in range(15):
            clothing_type = ClothingType.objects.create(name=f"clt_name_{i}")
            Clothing.objects.create(
                name=f"name_{i}", clothing_type=clothing_type, price=40.0
            )
        self.client.force_login(self.user)

    def test_retrieve_clothing(self) -> None:
        response = self.client.get(CLOTHING_LIST_URL)
        self.assertEquals(response.status_code, 200)
        clothing = Clothing.objects.all()
        self.assertEquals(
            list(response.context["clothing_list"]),
            list(clothing)[:20],
        )
        self.assertTemplateUsed(response, "catalog/clothing_list.html")

    def test_search_clothing_by_name(self) -> None:
        searched_name = "name_8"
        response = self.client.get(CLOTHING_LIST_URL, {"name": searched_name})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.context["clothing_list"][0],
            Clothing.objects.get(name=searched_name),
        )


class PrivateDesignerTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="testpass123",
            pseudonym="ABC123455",
        )
        for i in range(8):
            get_user_model().objects.create(
                username=f"user_{i}",
                password=f"pass_{i}",
                pseudonym=f"ABC1234{i}",
            )
        self.client.force_login(self.user)

    def test_retrieve_designer(self) -> None:
        response = self.client.get(DESIGNER_LIST_URL)
        self.assertEquals(response.status_code, 200)
        designer = Designer.objects.all()
        self.assertEquals(
            list(response.context["designer_list"]),
            list(designer)[:5],
        )
        self.assertTemplateUsed(response, "catalog/designer_list.html")

    def test_search_designer_by_username(self) -> None:
        searched_username = "user_4"
        response = self.client.get(
            DESIGNER_LIST_URL, {"username": searched_username}
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.context["designer_list"][0],
            Designer.objects.get(username=searched_username),
        )
