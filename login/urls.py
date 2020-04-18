from django.urls import path
from . import views
urlpatterns = [
	path('', views.loginPage, name='loginPage'),
	path('signup/', views.signup, name='signup'),
	path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
	path('logout/', views.logoutPage, name='logoutPage'),
]