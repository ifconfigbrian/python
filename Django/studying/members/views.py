from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Member

# here you define views that handle HTTP requests
# Create your views here.

def home(request):
    members_list = Member.objects.all()
    return render(request,'members/home.html',{'members_list':members_list})

def member_detail(request,id):
    member = get_object_or_404(Member, id=id)
    return render(request,'members/detail.html', {'member':member})

def member_list(request):
    members = Member.objects.all().order_by('name')
    return render(request,'members/member_list.html',{'name':members})