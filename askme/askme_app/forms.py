import django.forms as forms
from askme_app.models import Profile, User

class LoginForm(forms.Form):
    login = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    next = forms.CharField(widget=forms.HiddenInput, required=False)

class RegisterForm(forms.Form):
    login = forms.CharField(max_length=100)
    email = forms.EmailField()
    displayName = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('password_confirm'):
            raise forms.ValidationError('Passwords do not match')

class SettingsForm(forms.Form):
    email = forms.EmailField()
    displayName = forms.CharField(max_length=100)
    avatar = forms.ImageField(required=False)

class AskForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=5)
    text = forms.CharField(widget=forms.Textarea, min_length=10)
    tags = forms.CharField(max_length=100)

    def clean_tags(self):
        tags = [tag for tag in self.cleaned_data['tags'].split(' ') if tag]
        tags = list(set(tags))
        if len(tags) < 3:
            raise forms.ValidationError('At least 3 tags required')
        return tags
    
class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, min_length=5)