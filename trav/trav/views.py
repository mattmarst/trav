from django.http import HttpResponse

def index(request):

    html = 'Please click <a href=/listings/>here<a> to navigate to a list of properties currently available.'
    return HttpResponse(html)