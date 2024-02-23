import os
from django.core.mail import EmailMessage
from mysite.models import mysite  # Update the import statement and model name
path_pdf = '/home/jerryli/Downloads/output'
def get_users_with_emails():
    # Get all non-empty user email addresses
    return mysite.objects.exclude(email__isnull=True).exclude(email='').values_list('email', flat=True)

def configure_email_subject_and_content():
    # Customize your email subject and content here
    return '測試主旨', '測試內容'

def attach_file_to_email(email, file_path):
    # Attach file without reading it entirely into memory
    with open(file_path, 'rb') as file:
        email.attach('testpdf.pdf', file.read(), 'application/pdf')

def send_email_to_user(user_email,email_subject,email_content,path_pdf):

    email = EmailMessage(
        email_subject,
        email_content,
        '41041118@gm.nfu.edu.tw',
        [user_email],
        reply_to=['41041124@gm.nfu.edu.tw'],
    )

    attach_file_to_email(email, path_pdf)

    try:
        # Send email and handle errors
        email.send(fail_silently=False)
        print(f"Email sent successfully to {user_email}")
    except Exception as e:
        print(f"Error sending email to {user_email}: {e}")

def send_emails():
    users_with_emails = get_users_with_emails()
    email_subject , email_content = configure_email_subject_and_content()
    for user_email in users_with_emails:
        send_email_to_user(user_email,email_subject,email_content)

if __name__ == "__main__":
    send_emails()
