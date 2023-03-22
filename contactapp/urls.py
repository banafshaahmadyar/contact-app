from django.urls import path
from contactapp import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name="index"),
    path('insert', views.insertData, name="insertData"),
    path('update/<id>', views.updateData, name="updateData"),
    path('delete/<id>', views.deleteData, name="deleteData"),
    path('login',views.handleLogin,name="handleLogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('signup',views.signup,name="signup"),

]
