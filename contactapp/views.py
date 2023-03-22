from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.conf import settings

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


def deleteData(request, id):
    d = Contact.objects.get(id=id)
    d.delete()
    messages.warning(request, "Data deleted successfully")
    return redirect("/")


def SignupPage(request):
    return render(request, 'signup.html')


def LoginPage(request):
    return render(request, 'login.html')
