import base64
from datetime import datetime, timedelta
import requests
from NewBusinessAlert.BizAlert.utils.business_objects import parse_companies
from NewBusinessAlert.BizAlert.utils.email_util import send_newsletter
from NewBusinessAlert.BizAlert.utils.sublist import email_list


def send_daily_newsletter():
    # Flag to check if the newsletter has been sent
    newsletter_sent = False

    # Your API key and URL
    Apikey: str = 'b7300264-e1be-45cb-8712-405a1ade6796'
    api_key_base64 = f"Basic {base64.b64encode(Apikey.encode()).decode()}"
    date = datetime.now() - timedelta(days=1)
    yesterday: date = date.strftime("%Y-%m-%d")
    api_url = "https://api.company-information.service.gov.uk/advanced-search/companies"
    headers = {
        'Authorization': 'Basic c2hURVp4TURaRXdZNEJmZjk2M29IWkk3TV9IbVozaWFhbkdBSkVtTjo6'
    }

    # Parameters for the API request
    params = {
        "incorporated_from": yesterday,
        "size": 5000
    }

    # Make the API request
    response = requests.get(api_url, headers=headers, params=params)
    data = response.json()
    parsed_companies = parse_companies(data)

    # Check if the newsletter has already been sent
    if not newsletter_sent:
        # Send the newsletter
        send_newsletter(email_list, parsed_companies)

        # Update the flag to indicate that the newsletter has been sent
        newsletter_sent = True
        print("Newsletter sent!")


