from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView


urlpatterns =[
    #path('', views.HomePageView, name='kotisivu'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
