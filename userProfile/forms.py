from django import forms

from userProfile.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('like_cheese', 'favourite_hamster_name')
