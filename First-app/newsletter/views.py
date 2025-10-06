#from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


#def newsletter(request):
#   template = get_template('newsletter.html')
#   return HttpResponse(template.render({'request': request}))

def newsletter(request):
    return render(request, 'newsletter.html', {'request': request})

#def newsletter(request):
    #Sreturn HttpResponse("Subscribe to our newsletter")