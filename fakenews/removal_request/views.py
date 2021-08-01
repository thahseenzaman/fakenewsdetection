from django.shortcuts import render
from removal_request.models import Request
from login.models import Login
from user.models import RegUser
# Create your views here.
def removal(request):
    ko=str(request.session["user_id"])
    if request.method == "POST":
        obj = Request()
        obj.u_id=ko
        obj.request = request.POST.get("r")
        obj.status='pending'

        obj.save()

    return render(request,'removal_request/req.html')
# def reg(request):
#     oblist = RemovalRequest.objects.all()
#     context = {
#         'objval': oblist,
#     }
#
#     return render(request,'removal_request/reg.html')

def viewrew(request):
    obj=Request.objects.filter(status='pending')
    context={
        'objval':obj,
    }
    return render(request,"removal_request/view_request.html",context)


def unblock(request,idd,uid):
    obj=Request.objects.get(re_id=idd)
    obj.status='unblocked'
    obj.save()
    ne=Login.objects.get(user_id=uid)
    ne.type='user'
    ne.save()
    # oj=RegUser.objects.get(u_id=hid)
    # oj.status='pending'
    # oj.save()
    return viewrew(request)