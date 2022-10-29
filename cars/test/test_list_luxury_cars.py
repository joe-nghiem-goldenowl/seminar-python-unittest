from django.test import TestCase
from cars.models import Car
from django.test import Client
from unittest.mock import patch

client = Client()


class CarTests(TestCase):
    def setUp(self):
        Car.objects.create(price=20000, fuel_type='gasoline', name='Rover Range Rover Evoque')
        Car.objects.create(price=2000, fuel_type='diesel oil', name='Mercedes E300 AMG')

    # Example to test by mock
    # @patch('cars.services.services.CarServices.is_luxury_car', return_value=False)
    # def test_list_luxury_cars(self, is_luxury_car):
    #     response = client.get('/cars/')
    #     result = {'data': []}
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json(), result)

    def test_list_luxury_cars(self):
            response = client.get('/cars/')
            result = {
                'data': [
                    {
                        'fuel_type': 'gasoline',
                        'id': 1,
                        'name': 'Rover Range Rover Evoque',
                        'price': 20000.0
                    }
                ]
            }
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), result)
