from credit.models import Gift


def get_all_gifts(request):
    gifts = Gift.objects.all()
    return {'gifts': gifts}
