from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.conf import settings
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    data = Contact.objects.all()
    print(data)
    context = {"data": data}
    return render(request, "index.html", context)


def insertData(request):

    if request.method == "POST":
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        number = request.POST.get('number')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print(name, lastname, number, email, age, gender)
        query = Contact(name=name, lastname=lastname,
                        number=number, email=email, age=age, gender=gender)
        query.save()
        messages.success(request, "Data Inserted successfully")
        return redirect("/")
    return render(request, "index.html", context)


@login_required
def updateData(request, id):

    if request.method == "POST":
        name = request.POST['name']
        lastname = request.POST['lastname']
        number = request.POST['number']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        edit = Contact.objects.get(id=id)
        edit.name = name
        edit.lastname = lastname
        edit.number = number
        edit.email = email
        edit.age = age
        edit.gender = gender
        edit.save()
        messages.info(request, "Data Updated successfully")
        return redirect("/")

    d = Contact.objects.get(id=id)
    context = {"d": d}

    return render(request, "edit.html", context)


@login_required
def deleteData(request, id):
    d = Contact.objects.get(id=id)
    d.delete()
    messages.warning(request, "Data deleted successfully")
    return redirect("/")


def handleLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        myuser = authenticate(username=username, password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successful")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")

    return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            messages.info(request, "Password is not Matching")
            return redirect('/signup')

        try:
            if User.objects.get(username=username):
                messages.warning(request, "UserName is Taken")
                return redirect('/signup')

        except Exception as identifier:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request, "Email is Taken")
                return redirect('/signup')

        except Exception as identifier:
            pass

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, "User is Created Please Login")
        return redirect('/login')

    return render(request, "signup.html")


def handleLogout(request):
    logout(request)
    messages.success(request, "Logout Success")
    return redirect('/login')
