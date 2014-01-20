from accounts.models import Registration, UserProfile
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.http import Http404, HttpResponseNotFound
from django.template.context import RequestContext
from accounts.forms import RegistrationForm, EditUserForm, EditUserProfileForm
from django.contrib.sites.models import Site
from django.contrib.auth import logout
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from subs.models import Waist, Word

def activate(request, activation_key):
    """
    Activate account if valid activation_key and return to activation complete url,
    else return 404
    
    """
    
    activated = Registration.objects.activate_user(activation_key)
    if activated:
        #@todo:test it
        Registration.objects.create_profile(activated)
        return redirect('accounts_activation_complete')
    else:
        raise Http404


def register(request):
    """
    If POST, create new unactive user and redirect to complete registration
    Else display registration form
    
    """
    
    if request.method == 'POST':        
        form = RegistrationForm(request.POST)
        if form.is_valid():
            site = Site.objects.get_current()
            username, email, password = form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1']
            new_user = Registration.objects.create_inactive_user(username, email, password, site)
            
            return redirect('accounts_registration_complete')
    else:   
        form = RegistrationForm()
        
    return render_to_response('accounts/registration_form.html',
                              locals(),
                              context_instance=RequestContext(request))


def login_view(request):
    return render_to_response('accounts/login.html',
                              locals(),
                              context_instance=RequestContext(request))

@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts_login')


@login_required
def edit_profile(request):
    """
    Show form with fields to edit user info data.
    
    """
    title = _("Edit your profile")
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form_profile = EditUserProfileForm(request.POST, instance=user_profile)
        form_user = EditUserForm(request.POST, instance=user)
        if form_profile.is_valid() and form_user.is_valid():
            form_profile.save()
            form_user.save()
            return redirect("accounts_show_profile", user.username)

            
            
    else:
        # Without POST. Just display form
        form_profile = EditUserProfileForm(instance=user_profile)
        form_user = EditUserForm(instance=user)
    
    return render_to_response('accounts/edit_profile_form.html',
                              locals(),
                              context_instance=RequestContext(request))
    
def show_profile(request, username):
    """ view for each individual category page """

    

    user = get_object_or_404(User, username=username)
    user_profile = UserProfile.objects.get(user=user)    
    
    waists_len = len(Waist.objects.filter(user=request.user))
    words_len = len(Word.objects.filter(user=request.user))
    
    title = "%s: %s" % (_("Profile of"), user.username)

    return render_to_response('accounts/profile.html',
                              locals(),
                              context_instance=RequestContext(request))


