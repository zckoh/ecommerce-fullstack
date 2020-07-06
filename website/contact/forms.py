from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        label='Your Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Name"}))
    email_address = forms.EmailField(
        label='Your Email', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Email"}))
    subject = forms.CharField(max_length=200, label='Subject', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Your Subject"}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}), label='Your Message')
