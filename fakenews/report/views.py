from django.shortcuts import render
from report.models import Report
from django.http import HttpResponseRedirect
import datetime
from news.models import News
# Create your views here.


def detect(request,idd):
    obj_rep = Report.objects.get(id=idd) # from report
    r_nid = obj_rep.n_id #news id
    p_uid = obj_rep.n.u_id #news posted user id
    r_nm = obj_rep.u.name  # news reporter user id
    iid = obj_rep.u_id  # news reporter user id

    new_rep_cou = Report.objects.filter(n_id=r_nid) # report same news count
    coun = len(new_rep_cou)

    news_user_cou = Report.objects.filter(n__u_id=p_uid)  # report news count on same person
    coun_1 = len(news_user_cou)
    print(coun_1)

    n_rep_use_ = Report.objects.filter(u_id=iid)  # reporter count on
    r_iid = len(n_rep_use_)

    fake_count = News.objects.filter(u_id=p_uid,fake='Fake News Identified By Admin')  # fake count
    fake = len(fake_count)

    obj_news = News.objects.get(nid=obj_rep.n_id) #from news table
    st = obj_news.status #sentiment analysis value
    print(st)

    context = {
        'objval': obj_news,
        'st': st,
        'n_count':coun,
        'u_count': coun_1,
        'r_nm': r_nm,
        'r_idd': r_iid,
        'fa': fake,
    }
    if request.method=="POST" and 'g' in request.POST:
        print('g')
        obj_news.fake = 'Verified By Admin'
        obj_news.save()
        return HttpResponseRedirect('/report/rep/')

    elif request.method=="POST" and 'f' in request.POST:
        print('f')
        obj_news.fake = 'Fake News Identified By Admin'
        obj_news.save()
        return HttpResponseRedirect('/report/rep/')
    return render(request,'report/ap.html',context)


def rep(request):
    obj=Report.objects.filter(status='reported')
    context={
        'objval':obj,
    }
    return render(request, 'report/reap.html',context)


# def approve(request,idd):
#     obj=Report.objects.get(id=idd)
#     obj.status='approved'
#     obj.save()
#     return  rep(request)

def reject(request,idd):
    obj=Report.objects.get(id=idd)
    obj.status='rejected'
    obj.save()
    return  rep(request)


def repp(request):
    if request.method=="POST":
        obj=Report()
        obj.uid=request.method.get("u")
        obj.nid= request.method.get("n")
        obj.date= request.method.get("d")
        obj.report= request.method.get("r")
    return render(request, 'report/rep.html')


def repo(request):
    oblist = Report.objects.all()
    context = {
        'objval': oblist,
    }

    return render(request, 'report/repo.html',context)