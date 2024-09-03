from django.urls import path, include

from bases.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),    
]