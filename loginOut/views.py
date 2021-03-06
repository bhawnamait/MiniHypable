from django.contrib.auth.decorators import login_required

from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template.context_processors import csrf

from loginOut.forms import MyRegistrationForm


def login(request):
    c = {}
    c.update(csrf(request))

    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get("username", '')
    password = request.POST.get("password", '')
    user = auth.authenticate(username=username, password=password)
    global isLogin
    isLogin = False
    if user is not None:
        auth.login(request, user)
        isLogin = True
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')


@login_required
def loggedin(request):

    return render_to_response("loggedin.html", {'fullname': request.user.username})


def invalid_login(request):
    return render_to_response('invalid_login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')


def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
    else:
        form = MyRegistrationForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    print form.errors  # this line doesn't print anything
    return render_to_response('register.html', args)


def register_success(request):
    return render_to_response('register_success.html')
