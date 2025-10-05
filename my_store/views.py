#from django.http import HttpResponse
from django.http import HttpResponse
from django.template.loader import get_template


def newsletter(request):
    template = get_template('newsletter.html')
    return HttpResponse(template.render())


#def newsletter(request):
    #Sreturn HttpResponse("Subscribe to our newsletter")