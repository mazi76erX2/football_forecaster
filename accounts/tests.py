from typing import Dict, Union

from django.test import TestCase

from .forms.registration import RegistrationFormCustomTermsOfService

# from selenium.webdriver.firefox.webdriver import WebDriver


class RegistrationTestCase(TestCase):
    def setUp(self):
        # self.user = get_user_model().objects.create(username='test_user10', email='mazi76erx@gmail.com',
        #                                             password="Testing12#12")
        self.data: Dict[str, Union[str, bool]] = {
            'username': 'test_user10',
            'email': 'mazi76erx@gmail.com',
            'password1': "Testing12#12",
            'password2': "Testing12#12",
            'tos': True
        }

    # @classmethod
    # def setUpClass(cls):
    #     super().setUpClass()
    #     cls.selenium = WebDriver()
    #     cls.selenium.implicitly_wait(10)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.selenium.quit()
    #     super().tearDownClass()

    def test_valid_form(self):
        form = RegistrationFormCustomTermsOfService(data=self.data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data_invalid = self.data.copy()
        data_invalid['tos'] = False
        form = RegistrationFormCustomTermsOfService(data=data_invalid)
        self.assertFalse(form.is_valid())

    # def test_valid_form_client(self):
    #     self.client.post('/login/', data=self.data)

    # def test_login(self):
    #     self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
    #     username_input = self.selenium.find_element_by_name("username")
    #     username_input.send_keys('myuser')
    #     password_input = self.selenium.find_element_by_name("password")
    #     password_input.send_keys('secret')
    #     self.selenium.find_element_by_css_selector('.').click()


# class LoginTestCase(TestCase):
#     def setUp(self):
#         self.user = get_user_model().objects.create(username='test_user10', password="Testing12#12")
        # self.client = Client()