from django.contrib.auth.forms import UserCreationForm
from .models import HometendUser

class HometendUserForm(UserCreationForm):
    """모델 HometendUser의 Form
    
    class Meta:
        model: HometendUser
        fields: email, username, first_name, password

    """
    class Meta:
        model = HometendUser
        fields = ['email', 'username', 'first_name', 'password']
