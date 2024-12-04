from django import forms

class LoginForm(forms.Form):
    cpf = forms.CharField(max_length=11, label="CPF")
    senha = forms.CharField(widget=forms.PasswordInput, label="Senha")

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if len(cpf) != 11 or not cpf.isdigit():
            raise forms.ValidationError("O CPF deve ter 11 dígitos numéricos.")
        return cpf
