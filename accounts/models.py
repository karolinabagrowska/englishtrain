from django.db import models, transaction
from django.contrib.auth.models import User
import re
import random
from django.utils.hashcompat import sha_constructor
from django.template.loader import render_to_string
import settings
from subs.models import LANGS


SHA1_RE = re.compile('^[a-f0-9]{40}$')


class RegistrationManager(models.Manager):
    """
    Manager related with registration
    """
  
    def activate_user(self, activation_key):
        """
        Activate user if the activation key is correct
        """
        
        if SHA1_RE.search(activation_key):
            try:
                registration = self.get(activation_key=activation_key)
            except self.model.DoesNotExist:
                return False            
            user = registration.user
            user.is_active = True
            user.save()
            
            # Set activation key of the registration model as a default string to prevent double activation
            registration.activation_key = self.model.ACTIVATED
            registration.save()
            return user
        return False
    
    def create_profile(self, user):
        profile = UserProfile(user=user)
        profile.save()
    



    def create_inactive_user(self, username, email, password,
                             site, send_email=True):
        """
        Create a new, inactive ``User``, generate a
        ``RegistrationProfile`` and email its activation key to the
        ``User``, returning the new ``User``.

        By default, an activation email will be sent to the new
        user. To disable this, pass ``send_email=False``.
        
        """
        new_user = User.objects.create_user(username, email, password)
        new_user.is_active = False
        new_user.save()

        registration_profile = self._create_registration(new_user)

        if send_email:
            registration_profile.send_activation_email(site)
        return new_user


    def _create_registration(self, user):
        """
        Create a ``Registration`` model for a given
        ``User``, and return the ``Registration`` object
        
        The activation key for the ``RegistrationProfile`` will be a
        SHA1 hash, generated from a combination of the ``User``'s
        username and a random salt.
        
        """
        salt = sha_constructor(str(random.random())).hexdigest()[:5]
        activation_key = sha_constructor(salt + user.username).hexdigest()
        return self.create(user=user,
                           activation_key=activation_key)


class Registration(models.Model):  
    """
    Registration model, keep data to correct activate users
    """ 
    ACTIVATED = "ACTIVATED"    
     
    user = models.ForeignKey(User)
    activation_key = models.CharField(max_length=250)
    
    objects = RegistrationManager()
    

    
    def send_activation_email(self, site):
        """
        Send an activation email to the user associated with this
        ``Registration`` object.
        
        The activation email will make use of two templates:

        """
        ctx_dict = {'activation_key': self.activation_key,
                    'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
                    'site': site
                    }
        subject = render_to_string('accounts/activation_email_subject.txt',
                                   ctx_dict)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        
        message = render_to_string('accounts/activation_email.txt',
                                   ctx_dict)
        
        self.user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
        




class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    native_lang = models.CharField(max_length=50, blank=True, choices=LANGS)
    learning_lang = models.CharField(max_length=50, blank=True, choices=LANGS)
    about = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=500, blank=True)
    age = models.DateField(blank=True, null=True)
    
    

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

