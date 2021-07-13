from typing import Dict

field_dict: Dict[str, str] = {
    'type': "text",
    'minlength': '2',
    'maxlength': '150',
    'class': "form-control form-control-alternative",
}

username_dict: Dict[str, str] = field_dict.copy()
username_dict.update({'placeholder': 'Your Username'})

password1_dict: Dict[str, str] = field_dict.copy()
password1_dict.update({
    'placeholder': 'Your Password',
    'minlength': '8',
    'maxlength': '150',
    'pattern': '(?=.*)(?=.*[a-z])(?=.*[A-Z]).{8,}',
    'title': ('Must contain at least one number and one uppercase and '
              'lowercase letter, one special character and at least 8 '
              'or more characters'),
})

firstname_dict: Dict[str, str] = field_dict.copy()
firstname_dict.update({'placeholder': 'Your First Name'})

lastname_dict: Dict[str, str] = field_dict.copy()
lastname_dict.update({'placeholder': 'Your Surname'})

email_dict: Dict[str, str] = field_dict.copy()
email_dict.update({
    'placeholder': 'Your Email',
    'minlength': '5',
    'type': 'email',
})

choice_dict: Dict[str, str] = {'class': 'custom-select form-control form-control-alternative'}

date_of_birth_dict: Dict[str, str] = {
    'class': "form-control form-control-alternative datepicker",
    'placeholder': "Select date",
    'type': "text",
}

postal_code_dict: Dict[str, str] = {
    'minlength': '4',
    'maxlength': '4',
    'type': 'number',
    'class': "form-control form-control-alternative",
}

phone_number_dict: Dict[str, str] = {
    'minlength': '7',
    'maxlength': '13',
    'type': 'number',
    'class': "form-control form-control-alternative",
}