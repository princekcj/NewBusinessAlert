import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_newsletter(emails, new_companies):
    # Replace these with your email and SMTP server details
    sender_email = "cjbizent@gmail.com"
    sender_password = "D76CAFD57C65A6DAB43D79BC5AED3A8A3EE0"
    smtp_server = "smtp.elasticemail.com"
    smtp_port = 2525

    subject = "New Businesses Today"

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port, timeout=3000) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # Split companies into batches of 10
        for i in range(0, len(new_companies), 15):
            batch_companies = new_companies[i:i + 15]

            # Create the email content for the batch
            body = f"Dear recipient, Here are the new businesses created today:\n"
            company_names = [company.company_name for company in batch_companies]
            body += "\n".join(company_names)

            message = MIMEMultipart()
            message['From'] = sender_email
            message['Subject'] = subject

            # Use utf-8 encoding for the email body
            body = ''.join(char for char in body if ord(char) < 128)
            message.attach(MIMEText(body, 'plain', 'utf-8'))

            # Send the email to each recipient
            for email in emails:
                try:
                    text = message.as_string()
                    server.sendmail(sender_email, email, text)
                    print(f"Newsletter sent successfully to {email}!")
                except Exception as e:
                    print(f"Error sending newsletter to {email}: {e}")

    print("All batches sent successfully!")

# Example usage:
# send_newsletter(["recipient1@example.com", "recipient2@example.com"], new_companies_list)
