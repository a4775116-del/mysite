from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World! 這是我的第一個 Django 網頁！")

