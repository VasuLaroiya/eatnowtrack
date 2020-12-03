from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'favorite_food', 'favorite_hobby', 'user_age', 'user_goals', 'focus_area_1','focus_area_2','focus_area_3', 'user_height_in_inches', 'user_weight_in_lbs', 'user_sex']
        
class ProfilePreferencesForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['custom_grains_target','custom_protein_target','custom_dairy_target','custom_vegetables_target','custom_fruit_target','custom_aerobic_target','custom_muscle_strengthening_target']
