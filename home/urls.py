from django.contrib import admin
from django.urls import path
from home import views


# for changing the textstring's that is already made by admin
admin.site.site_header = "gsw Admin"
admin.site.site_title = "gsw Admin Portal"
admin.site.index_title = "Welcome to gsw Researcher Portal"

# if request comes it checks it's address acording to it it will render function according to its's path
# /about returns about function in view.py

urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contacts",views.contacts, name='contacts')
]
