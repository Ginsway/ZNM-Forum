from django.urls import path
from django.contrib.auth import views
from django.views.generic import TemplateView
from . import views as view

app_name = 'account'

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('register/', view.register, name='register'),
    path('change-password/', views.PasswordChangeView.as_view(
        template_name='account/change-password.html',
        success_url='/account/change-password-done/'
    ), name='change_password'),
    path('change-password-done/', views.PasswordChangeDoneView.as_view(template_name='account/change-password-done.html')
         , name='change_password_done'),
    path('my-information/', view.my_information, name='my_information'),
    path('edit-my-information/', view.edit_my_information, name='edit_my_information'),
    path('edit-image/', TemplateView.as_view(template_name='account/edit_image.html'), name='edit_image')
]
