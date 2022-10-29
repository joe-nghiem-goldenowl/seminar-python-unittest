class CarServices(object):

    @classmethod
    def is_luxury_car(cls, price):
        return price >= 10000
