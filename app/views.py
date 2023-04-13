from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        print(request.POST)
        return HttpResponse(f'<h1>{tn} data is inserted</h1>')
    return render(request,'insert_topic.html')
def insert_webpage(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()


        n=request.POST['n']
        url1=request.POST['url1']
        mail=request.POST['mail1']
        
        print(TO,n,url1,mail)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url1,email=mail)[0]
        WO.save()
        return HttpResponse(f'<h1>{n} data is inserted</h1>')

    return render(request,'insert_webpage.html')



def insert_accessrecords(request):
    if request.method=='POST':
        na=request.POST['n']
        WO=Webpage.objects.get_or_create(name=na)[0]
        WO.save()
        at=request.POST['at']
        da=request.POST['d']
        print(request.POST)
        AO=AccessRecord.objects.get_or_create(name=WO,author=at,date=da)[0]
        AO.save()
        return HttpResponse(f'<h1>{at} data is submitted</h1>')

    return render(request,'insert_accessrecords.html')