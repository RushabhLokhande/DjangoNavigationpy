
from django.http import HttpResponse
def index(request):
 return HttpResponse("<h1>Home Page</h1>")
def page1(request):
 return HttpResponse("Page 1 <a href='/'>Back</a>")
def page2(request):
 return HttpResponse("Page 2 <a href='/'>Back</a>")
def page3(request):
 return HttpResponse("Page 3<a href='/'>Back</a>")
def page4(request):
 return HttpResponse("Page 4 <a href='/'>Back</a>")
def page5(request):
 return HttpResponse("Page 5 <a href='/'>Back</a>")
