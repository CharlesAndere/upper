from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from minitwo.models import user
def minitwo(request):
    return HttpResponse("Hello and welcome to minitwo")
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def dashboard(request):
    data = user.objects.all();
    context = {'data': data}
    return render(request, 'dashboard.html', context)
@csrf_exempt
def loggingin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

    mydata = {'name':name, 'email':email, 'password':password}
    print(mydata)
    mine = user(name=name, email=email, password=password)
    mine.save()
    data = user.objects.all();
    context = {'data':data}
    return render(request, 'dashboard.html', context)
def deleteuser(request, id):
    deleteuser = user.objects.get(id=id)
    deleteuser.delete()
    return redirect('/dashboard')
def updateuser(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

    edituser = user.objects.get(id=id)
    edituser.name = name
    edituser.email = email
    edituser.password = password
    edituser.save()
    return redirect('/dashboard')
def edituser(request, id):
    data = user.objects.get(id=id)
    context = {'data': data}
    return render(request, 'updateuser.html', context)
