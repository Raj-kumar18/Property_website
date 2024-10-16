from django.shortcuts import render
from realapp.models import Property

# Create your views here.
def index(request):
    property = Property.objects.all()[0:3]
    return render(request, "index.html",{'property':property,})

def about(request):
    return render(request, "about.html")

def proper(request):
    property = Property.objects.all()
    return render(request, "property.html",{'property':property,})

def searchproperty(request):
    if request.method == 'POST':
        title = request.POST.get('title')
    property = Property.objects.filter(title=title).first()
    return render(request, "search.html",{'property':property,})


def property_detail(request,slug):
    property = Property.objects.filter(slug=slug)

    return render(request, "property_deatil_page.html",{'property':property,})
