from django.shortcuts import redirect, render
from .models import CustomUser
# Create your views here.

def users_list(request):  
    if request.method=="POST":
        CustomUser.objects.create(email=request.POST['email'],password=request.POST['password'], name=request.POST['name'])
        return redirect('users')
    else:
        users = CustomUser.objects.all()  
    return render(request, 'users.html', {'users':users})

def users_edit(request,id):
    if request.method=="POST":
        user = CustomUser.objects.get(pk=id)
        user.name = request.POST["name"]
        user.save()
        return redirect('users')
    else:
        user = CustomUser.objects.get(pk=id)
        return render(request, 'user_edit.html', {'user':user})  

def users_delete(request,id):
    if request.method=="POST":
        user = CustomUser.objects.get(pk=id)
        user.delete()
        return redirect('users')