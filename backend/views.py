from django.http import HttpResponse

def backend(request):
    return HttpResponse("Hello there")
