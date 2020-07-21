from registration.forms import RegistrationForm
from .models import User

class UserForm(RegistrationForm):
    class Meta:
        model = User
        fields=[
                'username',
                'password'
                ]
        widgets={
                'password':form.PasswordInput()
                }
