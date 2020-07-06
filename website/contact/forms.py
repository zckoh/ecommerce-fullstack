from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Nom',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "votre nom"}))
    email_address = forms.EmailField(
        label='Adresse e-mail', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "votre adresse e-mail"}))
    subject = forms.CharField(max_length=200, label='Sujet', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Sujet du courriel"}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}), label='Your Message')
