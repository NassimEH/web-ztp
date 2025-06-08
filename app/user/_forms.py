"""Custom forms for user authentication using allauth and crispy-forms modules.
This file is not used in the current implementation because
of an issue with the submit button in CustomLoginForm.
"""

from allauth.account.forms import LoginForm, SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CustomLoginForm(LoginForm):
    """Custom login form with crispy-forms integration.

    Adds a submit button to the allauth LoginForm.
    Allows customization of the login form using crispy-forms.

    However, the submit button does not work, while it works for CustomSignupForm.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("login", "Login"))


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("signup", "Sign Up"))
