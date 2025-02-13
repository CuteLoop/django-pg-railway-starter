# main/views.py
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from .forms import ContactMessageForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            # Save the message in the database
            contact_message = form.save()

            # Prepare the context for the email template
            context = {
                'name': contact_message.name,
                'message': contact_message.message,
            }
            # Render the email template (templates/emails/contact_confirmation.txt)
            email_body = render_to_string('emails/contact_confirmation.txt', context)

            try:
                # Send confirmation email to the user
                send_mail(
                    subject="Thank you for contacting us!",
                    message=email_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[contact_message.email],
                    fail_silently=False,
                )
                messages.success(request, "Your message has been received and a confirmation email has been sent to you.")
            except Exception as e:
                messages.error(request, "Your message was saved, but we couldn't send the confirmation email. Please try again later.")
                print("Email sending failed:", e)
            return redirect('contact')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactMessageForm()
    return render(request, 'contact.html', {'form': form})
