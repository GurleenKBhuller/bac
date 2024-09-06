from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
# Create your views here.


def about(request):
    return render(request, 'about.html')


def index(request):
    form = ContactForm()
    success_message = None  # Initialize success message variable

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Compose email
            contactsubject =  form.cleaned_data['subject']
            subject = f'Contact Form: {contactsubject}'
            email_message = f"Message from: {name} with email {email}\n\n{message}"
            from_email = email
            recipient_list = ['gurleenkaurbhuller@gmail.com']  # Replace with your recipient email
            
            # Send email
            send_mail(subject, email_message, from_email, recipient_list)
            success_message = "Message submitted successfully!"
            form = ContactForm()  # Reset the form after successful submission

    return render(request, 'index.html', {'form': form, 'success_message': success_message})
