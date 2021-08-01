from django.shortcuts import render
from video.models import Video
from django.core.files.storage import FileSystemStorage

# Create your views here.
def vide(request):
    po=str( request.session["user_id"])
    if request.method == "POST":
        obj = Video()
        obj.uid = po
        # obj.video= request.POST.get("video")
        myfile = request.FILES['video']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.video = myfile.name
        obj.save()

    return render(request, 'video/video_upload.html')
# def viewvid(request):
#     return render(request, 'video/view_vid_ply.html')


def viewv(request):
    re=request.session["user_id"]
    # user=Login.objects.get(user_id=re)
    # obj=Image.objects.filter(uid=user.user_id)
    obj=Video.objects.filter(uid=re)
    print(obj)
    context={
        'viewvideo':obj,
    }
    return render(request, 'video/video_view.html',context)

def viewvid(request):
    # re=request.session["user_id"]
    # user=Login.objects.get(user_id=re)
    # obj=Image.objects.filter(uid=user.user_id)
    obj=Video.objects.all()
    print(obj)
    context={
        'viewvideo':obj,
    }
    return render(request, 'video/view_vid_ply.html',context)

