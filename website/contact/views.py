from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from datetime import datetime
from pytz import timezone 
from .forms import ContactForm
from mailjet_rest import Client
import os

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # output what we have received
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email_address'])
            print(form.cleaned_data['subject'])
            print(form.cleaned_data['message'])

            # get timestamp of when form is received
            mauritius = timezone('Indian/Mauritius')
            mu_time = datetime.now(mauritius)

            mailjet = Client(auth=(settings.MJ_APIKEY_PUBLIC, settings.MJ_APIKEY_PRIVATE), version='v3.1')
            data = {
            'Messages': [
                {
                "From": {
                    "Email": "enquiryforwarding@tfnglun.com",
                    "Name": "Enquiries"
                },
                "To": [
                    {
                    "Email": "cnglun@intnet.mu",
                    "Name": "T.F. Ng Lun"
                    }
                ],
                "Subject": form.cleaned_data['subject'],
                "TextPart": "New enquiry form received from tfnglun.com/contact on " + mu_time.strftime('%Y-%m-%d %H:%M:%S') +"\n" + \
                        "\nName: " + form.cleaned_data['name'] + \
                        "\nEmail Address: " + form.cleaned_data['email_address'] + \
                        "\nMessage: \n\n" + form.cleaned_data['message'],
                }
            ]
            }
            result = mailjet.send.create(data=data)
            print(result.status_code)
            print(result.json())


            if (result.status_code != 200):
                return render(request, '500.html')
            else:
                return HttpResponseRedirect('thanks')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form' : form})

def thankyou_view(request):
    return render(request, 'contact/thanks.html')