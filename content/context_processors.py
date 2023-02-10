from content.models import Phone, Address, Email, Logo, WorkTime, TechCenter, Whatsapp, Title, DNS, Banner, HowToGo


def get_phone_numbers(request):
    phone_numbers = Phone.objects.all()
    return {'phone_numbers': phone_numbers}


def get_email(request):
    email = Email.objects.first()
    return {'email': email}


def get_address(request):
    address = Address.objects.first()
    return {'address': address}


def get_logo(request):
    logo = Logo.objects.first()
    return {'logo': logo}


def get_work_time(request):
    work_time = WorkTime.objects.first()
    return {'work_time': work_time}


def get_all_tech_centers(request):
    tech_centers = TechCenter.objects.all()
    return {'services': tech_centers}


def get_whatsapp(request):
    whatsapp = Whatsapp.objects.first()
    return {'whatsapp': whatsapp}


def get_title(request):
    title = Title.objects.first()
    return {'title': title}


def get_dns(request):
    dns = DNS.objects.first()
    return {'dns': dns}


def get_banners(request):
    banners = Banner.objects.all()
    return {'banners': banners}


def how_to_go(request):
    walks = HowToGo.objects.all()
    return {'walks': walks}
