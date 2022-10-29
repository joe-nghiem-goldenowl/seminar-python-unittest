from django.test import TestCase
from cars.services.services import CarServices


class CarTests(TestCase):
    # Example to know the order when excuting code
    # def setUp(self):
    #     print('This is set up')

    # def tearDown(self):
    #     print('This is teardown')

    # def setUpClass():
    #     print('This is setup class')

    # def tearDownClass():
    #     print('This is teardown class')

    def test_is_luxury_car(self):
        is_luxury_car = CarServices.is_luxury_car(20000)
        self.assertEqual(is_luxury_car, True)

    def test_not_luxury_car(self):
        is_luxury_car = CarServices.is_luxury_car(2000)
        self.assertEqual(is_luxury_car, False)
