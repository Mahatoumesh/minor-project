from django.shortcuts import render, redirect
from django.http import HttpResponse


def Homepage(request):
    return render(request, 'enroll/Home.html')

def studentdetails(request):
    return render(request, 'enroll/detail.html')


def signup(request):
    return render(request, 'enroll/signup.html')

def signin(request):
    return render(request, 'enroll/signin.html')