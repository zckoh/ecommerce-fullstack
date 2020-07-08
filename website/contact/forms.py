from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Nom',
        error_messages={
            'required': "ce nom n'est pas valide",
            'max_length': "le maximum nombre de charactère ne doit dépasser 100"
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "votre nom",
                'oninvalid': "this.setCustomValidity('Cette zone du formulaire ne doit pas être laissé vide')",
                'oninput': "setCustomValidity('')"
            }
        )
    )
    email_address = forms.EmailField(
        label='Adresse e-mail',
        error_messages={
            'required': "cette adresse mail n'est pas valide",
            'invalid' : "cette adresse mail n'est pas valide"
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "votre adresse e-mail",
                'oninvalid': "this.setCustomValidity('Cette zone du formulaire ne doit pas être laissé vide')",
                'oninput': "setCustomValidity('')"
            }
        )
    )
    subject = forms.CharField(
        max_length=200,
        label='Sujet',
        error_messages={
            'required': 'le sujet du courriel est manquant',
            'max_length': "le maximum nombre de charactère ne doit dépasser 200"
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Sujet du courriel",
                'oninvalid': "this.setCustomValidity('Cette zone du formulaire ne doit pas être laissé vide')",
                'oninput': "setCustomValidity('')"
            }
        )
    )
    message = forms.CharField(
        label='Your Message',
        error_messages={
            'required': "ce message n'est pas valide"
        },
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'oninvalid': "this.setCustomValidity('Cette zone du formulaire ne doit pas être laissé vide')",
                'oninput': "setCustomValidity('')"
            }
        )
    )
