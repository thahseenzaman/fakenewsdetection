from django.shortcuts import render
from feedback.models import Feedback
import datetime
# Create your views here.
def postfeed(request):
    bo=str(request.session["user_id"])
    if request.method=="POST":
        obj=Feedback()
        obj.u_id=bo
        obj.feedback=request.POST.get("f")
        obj.date=datetime.date.today()
        obj.save()

    return render(request,'feedback/post feed.html')



def viewfeed(request):
    oblist = Feedback.objects.all()
    context = {
        'objval': oblist,
    }

    return render(request,'feedback/feed.html',context)


