from typing import List, Union, Dict, Any

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from django_registration.forms import RegistrationFormTermsOfService
from . import username_dict, firstname_dict, lastname_dict, password1_dict, email_dict


class RegistrationFormCustomTermsOfService(RegistrationFormTermsOfService):
    class Meta(RegistrationFormTermsOfService.Meta):
        fields: List[str] = [
            "first_name",
            "last_name",
            User.USERNAME_FIELD,
            User.get_email_field_name(),
            "password1",
            "password2",
        ]

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Custom form for terms of service registration page that includes front end validation
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)

        password2_dict: Dict[str, Union[str, int]] = password1_dict.copy()
        password2_dict.update({'placeholder': 'Repeat your Password'})
        tos_dict: Dict[str, str] = {
            'name': 'agree-term',
            'id': 'agree-term',
            'class': 'agree-term',
            'onchange': "this.setCustomValidity(validity.valueMissing ? "
                        "'Please indicate that you accept the Terms of Service' : '');",
        }

        self.fields['first_name'].widget.attrs.update(firstname_dict)
        self.fields['last_name'].widget.attrs.update(lastname_dict)
        self.fields['username'].widget.attrs.update(username_dict)
        self.fields['email'].widget.attrs.update(email_dict)
        self.fields['password1'].widget.attrs.update(password1_dict)
        self.fields['password2'].widget.attrs.update(password2_dict)
        self.fields['tos'].widget.attrs.update(tos_dict)


class AuthenticationCustomForm(AuthenticationForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Custom form login page that includes front end validation
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(username_dict)
        self.fields['password'].widget.attrs.update(password1_dict)
