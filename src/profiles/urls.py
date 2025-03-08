from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.profile_list_view),
    path("<str:username>",views.profile_details_view)
]

