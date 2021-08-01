from django.shortcuts import render
from user.models import RegUser
from login.models import Login
from friends.models import Friends

# Create your views here.
def approv(request):
    obj = RegUser()
    obj.name = request.POST.get("id")
    obj.phone = request.POST.get("uid")
    obj.email = request.POST.get("m")
    obj.password = request.POST.get("p")
    obj.save()
    return render(request, 'user/approv_reject.html')

def frndr(request):
    return render(request, 'user/frnd_reqs.html')

def mana(request):
    return render(request, 'user/mana.html')

def regis(request):
    # uo=str(request.session["user_id"])
    if request.method=="POST":
        obj=RegUser()
        obj.name=request.POST.get("nam")
        obj.phone=request.POST.get("ph")
        obj.email = request.POST.get("em")
        obj.status = 'pending'
        obj.save()

        ob=Login()
        ob.username=request.POST.get('em')
        ob.password=request.POST.get('password')
        ob.type='user'
        ob.user_id=obj.u_id
        ob.save()

    return render(request, 'user/regis.html')


def register (request):
    if request.method=="POST":
        obj=RegUser()
        obj.uid=1
        obj.name=request.POST.get("uid")
        obj.phone=request.POST.get("m")
        obj.email = request.POST.get("p")
        obj.status = 'pending'
        obj.save()

    return render(request, 'user/register.html')
def sendr(request):
    return render(request, 'user/send_Request.html')
def blockuser(request):
    obj=RegUser.objects.filter(status='pending')
    context={
        'objval':obj,
    }
    return render(request,"user/reg.html",context)
def block(request,idd):
    obj=RegUser.objects.get(u_id=idd)
    obj.status='blocked'
    obj.save()
    ob=Login.objects.get(user_id=idd,type='user')
    ob.type='blocked'
    ob.save()
    return blockuser(request)



def search(request):
    if request.method=="POST" and 'search' in request.POST:
        # lg=request.session['user_id']
        # userid=Login.objects.get(id=lg)
        # usern=RegUser.objects.get(uid=userid.user_id)
        search=request.POST.get('news')
        ob=RegUser.objects.filter(name__icontains=search)
        context={
            'objval':ob,
        }
        return render(request,'user/search.html',context)
     # if request.method=="POST" and 'send request' in request.POST:
    return render(request,'user/search.html')
def sndrequest(request,idd):
    iid=str(request.session["user_id"])
    # s=RegUser.objects.get(uid=idd)
        # s=request.POST.get(id=idd)
    if Friends.objects.filter(u_id=iid,friend_id=idd):
        obj=Friends.objects.get(u_id=iid,friend_id=idd)
        obj.status='pending'
        obj.save()
    else:
        obj = Friends()
        obj.friend_id = idd
        obj.u_id = iid
        obj.status = "pending"
        obj.save()


    return search(request)
def approve(request,idd):

    ob=RegUser.objects.get(id=idd)

    return search(request)