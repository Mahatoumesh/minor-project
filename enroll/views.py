from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
# from .models import Room, Topic, Message, User
from .forms import MyUserCreationForm




# Create your views here.
def sign_up(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'enroll/signup.html', {'form':form})


def face(request):
    return render(request, 'enroll/face.html')

def detail(request):
    return render(request, 'enroll/detail.html')


def student(request):
    return render(request, 'enroll/student.html')




# def loginPage(request):
#     page = 'login'
#     if request.user.is_authenticated:
#         return redirect('home')

#     if request.method == 'POST':
#         email = request.POST.get('email').lower()
#         password = request.POST.get('password')

#         try:
#             user = User.objects.get(email=email)
#         except:
#             messages.error(request, 'User does not exist')

#         user = authenticate(request, email=email, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'Username OR password does not exit')

#     context = {'page': page}
#     return render(request, 'base/login_register.html', context)


# def logoutUser(request):
#     logout(request)
#     return redirect('home')


# def registerPage(request):
#     form = MyUserCreationForm()

#     if request.method == 'POST':
#         form = MyUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'An error occurred during registration')

#     return render(request, 'base/signup.html', {'form': form})
