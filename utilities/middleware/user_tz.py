# Adapted from Rogelio's answer:
# https://stackoverflow.com/a/73956012/13871578

from zoneinfo import ZoneInfo

from django.utils import timezone

class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            # get django_timezone from cookie
            tzname = request.COOKIES.get("django_timezone")
            if tzname:
                timezone.activate(ZoneInfo(tzname))
            else:
                timezone.deactivate()
        except Exception as e:
            timezone.deactivate()

        return self.get_response(request)
