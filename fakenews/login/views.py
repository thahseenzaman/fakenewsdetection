from django.shortcuts import render
from login.models import Login
from  django.http import HttpResponseRedirect

# Create your views here.
def log(request):
    if request.method == "POST":
        uname = request.POST.get("user")
        passw = request.POST.get("password")
        obj = Login.objects.filter(username=uname, password=passw)
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.user_id
            if tp == "admin":
                request.session["user_id"] = uid
                return render(request, 'temp/admin.html')
            elif tp == "user":
                request.session["user_id"] = uid
                return render(request, 'temp/user.html')

            elif tp == "blocked":
                request.session["user_id"] = uid
                return HttpResponseRedirect("/rem/rem/")
                # return render(request, 'removal_request/req.html')
            # elif tp == "police":
            #     request.session["uid"] = uid
            #     return render(request, 'temp/police.html')
            else:

                objlist = "Username or Password incorrect... Please try again...!"
                context = {
                    'msg': objlist,
                }
                return render(request, 'login/login.html', context)
        return render(request, 'login/login.html')
    return render(request, 'login/login.html')



# def req(request):
#     if request.method=="POST":
#         obj=Login()
#         obj.
#     return render(request,'login/req.html')