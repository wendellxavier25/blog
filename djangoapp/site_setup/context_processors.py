from .models import SiteSetup

def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first()

    return {'site_setup': setup}