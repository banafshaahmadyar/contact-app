from django.urls import path
from contactapp import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name="index"),
    path('insert', views.insertData, name="insertData"),
    path('update/<id>', views.updateData, name="updateData"),
    path('delete/<id>', views.deleteData, name="deleteData"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),


]
