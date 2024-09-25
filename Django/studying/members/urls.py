from django.urls import path
from . import views
from .views import member_list

# patterns should be lowercase

urlpatterns = [
    path('',views.home,name='home'),
    path('members/',member_list,name='member_list'),
    path('member/<int:id>/', views.member_detail, name='member_detail'),
    
]