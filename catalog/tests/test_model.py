from django.test import TestCase

from catalog.models import ClothingType, Size, Clothing, Material

from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_material_str(self) -> None:
        material = Material.objects.create(name="test")
        self.assertEqual(str(material), material.name)

    def test_clothing_type_str(self) -> None:
        clothing_type = ClothingType.objects.create(name="test")
        self.assertEqual(str(clothing_type), clothing_type.name)

    def test_size_str(self) -> None:
        size = Size.objects.create(name="test", description="test")
        self.assertEqual(str(size), f"{size.name} ({size.description})")

    def test_clothing_str(self) -> None:
        clothing = Clothing.objects.create(
            name="test",
            price=10.0,
            clothing_type=ClothingType.objects.create(name="test"),
        )
        self.assertEqual(str(clothing), f"{clothing.name} - ${clothing.price}")

    def test_designer_str(self) -> None:
        designer = get_user_model().objects.create_user(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_second",
        )
        self.assertEqual(
            str(designer),
            f"{designer.username} {designer.first_name} {designer.last_name}",
        )

    def test_create_designer_with_pseudonym(self) -> None:
        username = "test"
        password = "test123"
        pseudonym = "DER12345"
        designer = get_user_model().objects.create_user(
            username=username, password=password, pseudonym=pseudonym
        )
        self.assertEqual(designer.username, username)
        self.assertEqual(designer.pseudonym, pseudonym)
        self.assertTrue(designer.check_password(password))
