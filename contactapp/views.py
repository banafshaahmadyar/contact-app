from django.shortcuts import render, redirect
from .models import Contact

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
        return redirect("/")
    return render(request, "index.html")


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
        return redirect("/")

    d = Contact.objects.get(id=id)
    context = {"d": d}

    return render(request, "edit.html", context)


def deleteData(request, id):
    data = Contact.objects.all()
    print(data)
    context = {"data": data}

    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")
