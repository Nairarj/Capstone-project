from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from restaurant.models import menu          # your menu model
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # create some test menu items
        menu.objects.create(title="IceCream", price=80, inventory=100)
        menu.objects.create(title="Pizza",     price=120, inventory=50)
        menu.objects.create(title="Burger",    price=90,  inventory=30)

    def test_getall(self):
        # call your Menu list endpoint
        response = self.client.get("/restaurant/menu/")
        # get all menu items from DB
        items = menu.objects.all()
        # serialize them
        serializer = MenuSerializer(items, many=True)

        # status should be 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # response data should match serializer data
        self.assertEqual(response.data, serializer.data)
