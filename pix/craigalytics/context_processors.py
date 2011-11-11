def get_useful_constants(request):
    from django.conf import settings
    return {'MEDIA_URL': settings.MEDIA_URL, 'SUBSITE_URL':settings.SUBSITE_URL}
