from django.shortcuts import render
from pr.models import Pr

# Create your views here.
def app(request):
    if request.method == "POST":
        obj = Pr()
        obj.uid = request.POST.get("u")
        obj.request = request.POST.get("r")
        obj.date = request.POST.get("d")
        obj.save()


    return render(request,'pr/app.html')


def block(request):
    return render(request, 'pr/block.html')
def pro(request):




    return render(request, 'pr/pro.html')
def rej(request):
    return render(request, 'pr/rej.html')


from django.shortcuts import render

# Create your views here.
