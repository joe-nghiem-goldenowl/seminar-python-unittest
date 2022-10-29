from django.http import JsonResponse
from .models import Car
from .services.services import CarServices


def list_luxury_cars(request):
    cars = Car.objects.all()
    data = []
    for car in cars:
        if CarServices.is_luxury_car(car.price):
            data.append(car.to_json())
    return JsonResponse({'data': data})
