from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
   path('signup/', views.signup, name='signup'),
   path('login/', views.login, name='login'),
   path('logout/', views.logout, name='logout'),
   path('<int:pk>/update/', views.update, name='update'),
   path('<int:pk>/profile/', views.profile, name='profile'),
   path('<int:pk>/password/', views.pw_update, name='pw_update'),

]