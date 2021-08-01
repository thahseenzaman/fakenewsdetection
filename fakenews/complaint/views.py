from django.shortcuts import render
from complaint.models import Complaint
from django.db.models import Max,Min
# Create your views her


def viewcomplaint(request):
    oblist = Complaint.objects.filter(replay='pending')
    context = {
        'objval': oblist,
    }

    return render(request,'complaint/view.html',context)

def reply(request,idd):
    # obj=Complaint.objects.get(cid=idd)
    # context={
    #     'objval':obj,
    # }
    if request.method=="POST":
        ob=Complaint.objects.get(cid=idd)
        ob.replay=request.POST.get('rep')
        ob.save()
    return render(request,'complaint/re.html')


def complaint(request):
    po=str(request.session["user_id"])
    if request.method=="POST":
        obj=Complaint()
        obj.u_id =po
        obj.complaint=request.POST.get("c")
        obj.date = request.POST.get("d")
        obj.replay = 'pending'
        obj.save()

    return render(request,'complaint/complaint.html')


def min(request):
    obj=Complaint.objects.all().aggregate(Min("cid"))
    context={
        'mininum':obj,
    }
    return render(request,"complaint/view.html",context)