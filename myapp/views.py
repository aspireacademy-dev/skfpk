from django.shortcuts import render
from django.http import HttpResponse
from .models import Header
from .models import headerbox
from .models import Before_Footer_Upcoming_Events, contact,contacttest,contactlast
# Create your views here.
def home(request):
    obj=Header.objects.all
    obj1=headerbox.objects.all
    obj2=Before_Footer_Upcoming_Events.objects.all
    return render(request,'index.html',{'all':obj,'box':obj1,'events':obj2})
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about-us.html')
def Contact(request):
    if request.method == "POST":
        first = request.POST.get('first', '')
        last = request.POST.get('last', '')
        print(first, last)
        Contact = contact(fname=first, lname=last)
        Contact.save()
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')

def course(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname','')
        lastname=request.POST.get('lastname','')
        print(firstname,lastname)
        course=contacttest(firstname=firstname,lastname=lastname)
        course.save()
        return render(request,'course-details.html')
    else:
        return render(request, 'course-details.html')


def courses(request):
    return  render(request,'courses.html')
def elements(request):
    return render(request,'elements.html')
def blog(request):
    if request.method=="POST":
        firstname1=request.POST.get('firstname1','')
        lastname1=request.POST.get('lastname1','')
        print(firstname1,lastname1)
        blog=contactlast(firstname1=firstname1,lastname1=lastname1)
        blog.save()
        return render(request, 'blog.html')
    else:
        return render(request, 'blog.html')





def blogdetails(request):
    return render(request,'single-blog.html')
def Administration(request):
    return HttpResponse("Administration Page")
def Migrations(request):
    return HttpResponse("Migrations Page")



