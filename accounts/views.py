from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.conf import settings
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponse, HttpRequest

from django_registration.backends.activation.views import RegistrationView

from .forms.registration import RegistrationFormCustomTermsOfService, AuthenticationCustomForm
from .models import UserProfile
from .forms.registration_profile import UserProfileForm, UserForm


class RegistrationTermsOfServiceView(SuccessMessageMixin, RegistrationView):
    form_class = RegistrationFormCustomTermsOfService
    email_body_template = "registration/email/activation_email.html"
    email_subject_template = "django_registration/activation_email_subject.txt"
    success_message = "You were successfully logged in"

    def send_activation_email(self, user: User) -> None:
        """
        Send the activation email. The activation key is the username,
        signed using TimestampSigner.

        """
        activation_key = self.get_activation_key(user)
        context = self.get_email_context(activation_key)
        context["site_name"] = settings.SITE_NAME
        context["user"] = user

        subject = render_to_string(
            template_name=self.email_subject_template,
            context=context,
            request=self.request,
        )
        # Force subject to a single line to avoid header-injection
        # issues.
        subject = "".join(subject.splitlines())
        message = render_to_string(
            template_name=self.email_body_template,
            context=context,
            request=self.request,
        )
        user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL, html_message=message)


class LoginCustomView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationCustomForm
    success_message = "You were successfully logged in"


@login_required
@transaction.atomic
def update_profile(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        userprofile, created = UserProfile.objects.get_or_create(user=request.user)
        profile_form = UserProfileForm(request.POST, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('home_page')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        userprofile, created = UserProfile.objects.get_or_create(user=request.user)
        profile_form = UserProfileForm(instance=userprofile)
    return render(request, 'update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
    })
