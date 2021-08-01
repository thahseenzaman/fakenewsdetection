from django.shortcuts import render
from friends.models import Friends
from user.models import RegUser


# Create your views here.
def frnd_key(request):
    if request.method=="POST":
        obj=Friends()
        obj.uid ="2"
        obj.friend_id=request.POST.get("fid")
        obj.status = "requested"
        obj.save()
    return render(request, 'friends/frnd_key.html')


def send_reg(request):
    oblist = Friends.objects.all()
    context = {
        'objval': oblist,
    }
    return render(request,'friends/send_req.html',context)


def view_reg(request):
    eid=str(request.session["user_id"])
    obj=Friends.objects.filter(friend_id=eid,status="pending")
    context={
        'value':obj,
    }
    return render(request,'friends/view_friend.html',context)



def fapprove(request,idd):
    obj=Friends.objects.get(id=idd)
    obj.status='approved'
    obj.save()
    return view_reg(request)


def freject(request,idd):
    obj=Friends.objects.get(id=idd)
    obj.status='rejected'
    obj.save()
    return view_reg(request)
