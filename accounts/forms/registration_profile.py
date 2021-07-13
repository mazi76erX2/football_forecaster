from typing import Any
from datetime import datetime

from django.contrib.auth import get_user_model
from django.forms import ModelForm, ChoiceField, Select
from django.conf import settings

from ..models import UserProfile
from . import username_dict, firstname_dict, lastname_dict, email_dict, field_dict, choice_dict, date_of_birth_dict, \
              postal_code_dict, phone_number_dict

User = get_user_model()


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        username_dict.update({'id': "input-username"})
        email_dict.update({'id': "input-email"})
        firstname_dict.update({'id': "input-first-name"})
        lastname_dict.update({'id': "input-last-name"})

        self.fields['first_name'].widget.attrs.update(firstname_dict)
        self.fields['last_name'].widget.attrs.update(lastname_dict)
        self.fields['username'].widget.attrs.update(username_dict)
        self.fields['email'].widget.attrs.update(email_dict)


class UserProfileForm(ModelForm):
    gender = ChoiceField(choices=UserProfile.GenderChoices.choices, widget=Select(attrs=choice_dict))
    province = ChoiceField(choices=settings.PROVINCES, widget=Select(attrs=choice_dict))
    country = ChoiceField(choices=settings.COUNTRIES, widget=Select(attrs=choice_dict))
    preferred_language = ChoiceField(choices=settings.LANGUAGES, widget=Select(attrs=choice_dict))

    class Meta:
        model = UserProfile
        fields = ('gender', 'dob', 'address', 'phone_number', 'suburb', 'city', 'postal_code', 'province', 'country',
                  'preferred_language')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.fields['dob'].widget.attrs.update(date_of_birth_dict)
        self.fields['phone_number'].widget.attrs.update(phone_number_dict)
        self.fields['address'].widget.attrs.update(field_dict)
        self.fields['suburb'].widget.attrs.update(field_dict)
        self.fields['city'].widget.attrs.update(field_dict)
        self.fields['postal_code'].widget.attrs.update(postal_code_dict)
