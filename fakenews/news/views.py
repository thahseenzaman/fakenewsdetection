from django.shortcuts import render
from news.models import News
from report.models import Report
import datetime
from django.core.files.storage import FileSystemStorage
import datetime

import nltk
import nltk.sentiment
import nltk.sentiment.util


# Create your views here.
def fakec(request):
    return render(request, 'news/fake_chance_table.html')

def news(request):
    nt=str(request.session["user_id"])
    if request.method=="POST":
        obj=News()
        obj.u_id=nt
        obj.news=request.POST.get("news")
        obj.date=datetime.date.today()
        obj.fake = 'Not Verified Yet..'

        myfile = request.FILES['im']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        image = myfile.name



        n = request.POST.get('news')
        sid = nltk.sentiment.vader.SentimentIntensityAnalyzer()
        compound = sid.polarity_scores(n)["compound"]
        print(compound)
        f = 0
        if compound > 0:
            f = 1
            print("positive")
        elif compound < 0:
            f = -1
            print("negative")
        else:
            f = 0
            print("nu")

        obj.status = f
        obj.img = image
        obj.save()
    return render(request,'news/news.html')


def update(request):
    obj=News.objects.all()
    context={
        'objval':obj,
    }
    return render(request, 'news/update_table.html',context)

def updatenew(request,idd):
    obj=News.objects.get(nid=idd)
    context={
        'objval':obj,
    }
    nt = str(request.session["user_id"])
    if request.method == "POST":
        obj = News.objects.get(nid=idd)
        # obj.u_id = nt
        obj.news = request.POST.get("news")
        obj.date = request.POST.get("date")
        obj.save()
    return render(request,"news/up.html",context)


def viewn(request):
    oblist = News.objects.all()
    context = {
        'objval': oblist,
    }

    return render(request,'news/viewnews.html',context)


def viewfake(request):
    oblist = News.objects.all().exclude(u_id=str(request.session["user_id"]))
    context = {
        'objval': oblist,
    }
    return render(request,'news/view_fake.html',context)

def newspublic(request):
    obj=News.objects.all()
    context={
        'objval':obj,
    }
    return render(request,"news/newsview_publi.html",context)



def reason(request,idd):
    ho=str(request.session["user_id"])
    obj = News.objects.get(nid=idd)
    if request.method=="POST":

        ob=Report()
        ob.reason=request.POST.get('re')
        ob.u_id= ho
        ob.n_id= idd
        ob.n_u_id = obj.u_id
        ob.date=datetime.date.today()
        ob.time=datetime.datetime.now()
        ob.status='reported'
        ob.save()

        # return viewfake(request)
    return render(request,'news/reason.html')