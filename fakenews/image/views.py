from django.shortcuts import render
from image.models import Image
from django.core.files.storage import FileSystemStorage

from login.models import Login
# Create your views here.


def viewimage(request):
    if request.method=="POST":
        obj=Image()
        obj.uid =request.session["user_id"]
        # obj.image=request.POST.get("com")
        myfile=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.image=myfile.name
        obj.save()

    return render(request, 'image/image upload.html')


def uploadimage(request):
    re=request.session["user_id"]
    # user=Login.objects.get(user_id=re)
    # obj=Image.objects.filter(uid=user.user_id)
    obj=Image.objects.filter(uid=re)
    print(obj)
    context={
        'viewimages':obj,
    }
    return render(request, 'image/vimg.html',context)


def imagepub(request):
    # re=request.session["user_id"]
    # user=Login.objects.get(user_id=re)
    # obj=Image.objects.filter(uid=user.user_id)
    obj=Image.objects.all()
    print(obj)
    context={
        'viewimages':obj,
    }
    return render(request, 'image/view_img.html',context)




