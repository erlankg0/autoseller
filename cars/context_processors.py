from cars.models import Brand


def get_all_brands(request):
    brands = Brand.objects.all()[0:44]
    return {'brands': brands}
