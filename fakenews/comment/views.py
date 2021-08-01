from django.shortcuts import render
from comment.models import Comment
import datetime

# Create your views here.
def viewcomment(request):
    oblist=Comment.objects.all()
    context={
        'objval':oblist,
    }
    return render(request,'comment/comment.html',context)

def postcomment(request):
    de=str(request.session["user_id"] )
    if request.method=="POST":
        obj=Comment()
        obj.uid =de
        obj.comment=request.POST.get("com")
        obj.date = datetime.datetime.today()
        obj.save()

    return render(request,'comment/post comment.html')