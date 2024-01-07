class Company:
    def __init__(self, data):
        self.company_name = data['company_name']
        self.company_number = data['company_number']
        self.company_status = data['company_status']
        self.company_type = data['company_type']
        self.date_of_creation = data['date_of_creation']
        self.registered_office_address = data['registered_office_address']

    def __str__(self):
        return f"{self.company_name} ({self.company_number}) - {self.company_status}"

def parse_companies(data):
    companies = []
    for item in data['items']:
        company = Company(item)
        companies.append(company)
    return companies

