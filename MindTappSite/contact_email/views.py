from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Recipient

def contact(request):
    if request.method == 'POST':
        subject = 'New contact request from ' + request.POST['name']
        if 'jobTitle' in request.POST:
            subject = subject + ', the ' + request.POST['jobTitle']
        if 'company' in request.POST:
            subject = subject + ' of company ' + request.POST['company']

        message = 'Message:\n' + request.POST['message'] + '\nPhone number: ' + request.POST['phone'] + '\nEmail: ' + request.POST['email']
        recipients = list(Recipient.objects.all())
        for i, recipient in enumerate(recipients):
            recipients[i] = str(recipient)

        send_mail(
            subject,
            message,
            'MindTAPP Website',
            recipients,
        )

        #return 200, does not update page directly but lets it know success
        return HttpResponse()
