from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from accounts.forms import UserForm, LoginForm
from django.contrib.auth import authenticate, login


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print username, password
        user = authenticate(username=username, password=password)
        print user
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        form = LoginForm()

    template = 'accounts/login.html'
    return render(request, template, {'form': form})


def register(request):
    registered = False
    if request.method == 'POST':
        form = UserForm(data = request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            registered = True
        else:
            form.errors
    else:
        form = UserForm()

    template = 'accounts/register.html'
    return render(request, template, {'form': form})