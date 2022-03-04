from django.contrib.auth.forms import UserCreationForm
from .models import HometendUser

class HometendUserForm(UserCreationForm):
  class Meta:
    model = HometendUser
    fields = ['email', 'username', 'password']