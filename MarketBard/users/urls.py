from django.urls import path
from users.views import profile, register, login

app_name = 'users'

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('register/', register, name='register')

]
