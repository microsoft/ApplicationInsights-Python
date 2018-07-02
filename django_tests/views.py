from django.http import HttpResponse, Http404
from django.template.response import TemplateResponse

def home(request):
    return HttpResponse("Welcome home")

def logger(request):
    request.appinsights.client.track_trace("Logger message", {"property": "value"})
    return HttpResponse("We logged a message")

def thrower(request):
    raise ValueError("This is an unexpected exception")

def errorer(request):
    raise Http404("This is a 404 error")

def echoer(request):
    return HttpResponse(request.appinsights.request.id)

def getid(request, id):
    return HttpResponse(str(id))

def returncode(request, id):
    return HttpResponse("Status code set to %s" % id, status=int(id))

def templater(request, data):
    return TemplateResponse(request, 'template.html', {'context': data})

class classview:
    def __call__(self, request):
        return HttpResponse("You called a class.")
