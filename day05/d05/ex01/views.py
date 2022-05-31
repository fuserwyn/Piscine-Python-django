
from django.http import HttpRequest, HttpResponse


def init(request: HttpRequest):
    try:
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)