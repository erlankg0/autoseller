from cars.models import Brand, Vehicle


def get_all_brands(request):
    brands = Brand.objects.all()[0:44]
    return {'brands': brands}


def get_all_vehicle_types(request):
    vehicles = Vehicle.objects.all()
    return {"vehicles": vehicles}
