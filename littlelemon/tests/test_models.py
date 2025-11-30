from django.test import TestCase
from restaurant.models import menu

class MenuModelTest(TestCase):
    def test_get_item(self):
        # create a menu item
        item = menu.objects.create(
            title="IceCream",
            price=80,
            inventory=100
        )

        # check the string representation
        self.assertEqual(str(item), "IceCream : 80")