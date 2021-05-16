from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=255, required=True)
    last_name = forms.CharField(label='Last name', max_length=255, required=True)
    email = forms.EmailField(label='Email', max_length=255, required=True)
    password = forms.CharField(label="Password",widget=forms.PasswordInput, required=True)
    password_confirmation = forms.CharField(label='Password confirmation', widget=forms.PasswordInput, required=True)

    def clean_email(self):
        email=self.cleaned_data.get("email")

        try:
            AuthUser.object.get(email=email)
            except
        AuthUser.DoesNotExist:
            
        if user:
            raise forms.ValidationError("Email is already taken")
        return email





        label='Password',
        widget=forms.PasswordInput,
        required=True,
        # help_text=password_validators_help_text_html()
    )
