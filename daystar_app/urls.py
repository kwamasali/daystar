app_name = 'daystar_app'
from daystar_app import views
from django.urls import path
from .views import SignUpView
from django.views.generic.base import TemplateView
 

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboards/', TemplateView.as_view(template_name='daystar-app/dashboards.html'), name='dashboard'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', views.logoutview, name='logout'),
    path('babies/', views.babies, name='babies'),
    path('payment/', views.payment, name='payment'),
    path('sitters/', views.sitter, name='sitter'),
    path('dolls-shop/', views.dollshop, name='dollshop'),
    path('displays/', views.display, name='display'),
    path('checkin/', views.checkin, name='checkin'),
    path('all-babies/', views.babydisplay, name='babydisplay'),
    path('all-payments/', views.paymentdisplay, name='paymentdisplay'),
    path('all-sitters/', views.sitterdisplay, name='sitterdisplay'),
    path('all-inventory/', views.inventorydisplay, name='inventorydisplay'),
    path('all-checkins/', views.checkindisplay, name='checkindisplay'),
]