from django.shortcuts import render, redirect
from accounts.forms import UserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register(request):
    registered = False
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            messages.success(request, "Thank you for registering.")
            return redirect('login')
        else:
            form.errors
    else:
        form = UserForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not request.POST.get('remember_me'):
            request.session.set_expiry(0)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print username, password
        user = authenticate(username=username, password=password)
        print user
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, "You are successfully logged in.")
                return redirect('index')
            else:
                messages.error(request, "Your account is disabled.")
        else:
            messages.error(request, "Invalid login details.")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required()
def logout_view(request):
    logout(request)
    messages.success(request, "You are successfully Signed out.")
    return redirect('login')
