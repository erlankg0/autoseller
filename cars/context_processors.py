from cars.models import Brand, BodyType, Transmissions, DriveUnit, Fuel, Years
import datetime
from credit.forms import TradeInForm


def get_all_brands(request):
    brands = Brand.objects.all()[0:44]
    return {'brands': brands}


def get_all_vehicle_types(request):
    vehicles = BodyType.objects.all()
    return {"bodies": vehicles}


def get_all_years(request):
    years = Years.objects.all()
    return {"years": years}


def get_all_transmissions(request):
    transmissions = Transmissions.objects.all()
    return {"transmissions": transmissions}


def get_all_drive_units(request):
    drive_units = DriveUnit.objects.all()
    return {"drive_units": drive_units}


def get_all_fuels(request):
    fuels = Fuel.objects.all()
    return {"fuels": fuels}


def trade_in(request):
    form = TradeInForm()
    return {'trade': form}
