from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import register, logout

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html',
    extra_context = {'title' : 'Laze Login'}), name="login"),
    url(r'^logout/$', logout),
    url(r'^register/$', register),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name="password_reset/password_reset.html",
             email_template_name="password_reset/password_reset_email.html", 
             extra_context = {'title' : 'Forgot your password?'}),
         name="reset"),
    # # the password has been reset password reset done
    path('password-reset/success',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset/password_reset_done.html',
             extra_context = {'title' : 'Forgot your password?'}),
         name="password_reset_done"),
    # # the url sent from email
    path('password-reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset/password_reset_confirm.html',
             extra_context = {'title' : 'Laze Password Reset'}),
         name="password_reset_confirm"),

    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset/password_reset_complete.html',
             extra_context = {'title' : 'Laze Password Reset Successful'}),
         name="password_reset_complete"),
]
