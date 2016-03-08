from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context_processors import csrf

from userProfile.forms import UserProfileForm


@login_required
def user_profile(request):

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/loggedin')
    else:
        form = UserProfileForm(instance=request.user.profile)

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('profile.html', args)
