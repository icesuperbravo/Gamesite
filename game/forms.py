from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from .models import Profile, Game
from django.contrib.auth.models import User
from django.forms import ModelForm
from hashlib import md5

#User = get_user_model()
#print (User)

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            print (user)
            if not user:
                raise forms.ValidationError("This user does not exist!")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword!")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
            model = User
            #print (UserDetails)
            fields = [
                'username',
                'first_name',
                'last_name',
                'email',
                'email2',
                'password'
            ]

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email

class ProfileForm(forms.ModelForm):

    usertype = forms.TypedChoiceField( label = "Which role do you want to be registered as?",
                                       choices = ((0, "Player"), (1, "Developer")),
                                       coerce=int,
                                       widget = forms.RadioSelect,
                                       required = True,
                                       )
    class Meta:
        model = Profile
        fields = ('usertype',)

class GameForm(ModelForm):
    class Meta:
        model = Game

        fields = ['title', 'description', 'price', 'image_url', 'game_url']

class DeleteGameForm(ModelForm):
    class Meta:
        model = Game
        fields = []

class BuyGameForm(ModelForm):
    class Meta:
        model = Game
        fields = []
# class BuyGameForm(ModelForm):
#     class Meta:
#         model = Game
#         fields = []

class BuyGameForm(forms.Form):
    amount = forms.DecimalField(widget=forms.HiddenInput(), required= False, initial = 15)
    pid = forms.CharField(widget=forms.HiddenInput(), initial='mytestsale' )
    sid = forms.CharField(widget=forms.HiddenInput(), initial='tester')
    success_url = forms.URLField(widget=forms.HiddenInput(), initial='http://localhost:8000/payment/success')
    cancel_url = forms.URLField(widget=forms.HiddenInput(), initial='http://localhost:8000/payment/cancel')
    error_url = forms.URLField(widget=forms.HiddenInput(), initial='http://localhost:8000/payment/error')
    checksum = forms.CharField(widget=forms.HiddenInput(),required= False)


    # def clean_checksum(self):
    #     amount = self.cleaned_data.get('amount')
    #     pid = self.cleaned_data.get('pid')
    #     sid = self.cleaned_data.get('sid')
    #     secret_key = '6cd118b1432bf22942d93d784cd17084'
    #     checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, secret_key)
    #     print (checksumstr)
    #     m = md5(checksumstr.encode("ascii"))
    #     print (m)
    #     checksum = m.hexdigest()
    #     print (checksum)
    #     print("new clean checksum method!")
    #     return checksum
