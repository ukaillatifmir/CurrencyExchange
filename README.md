# CurrencyExchange
Currency Management System
Welcome to the Currency Management System! This Django application allows users to manage and convert currencies easily. It includes functionalities for viewing, creating, updating, and deleting currencies, as well as accessing currency rates and converting amounts between different currencies.

# Technologies Used
1. Django - 5
2. Python Versions :  3.12.7
# Installation
To get started with the Currency Management System, follow these steps:

1. Clone the repository: git clone https://github.com/ukaillatifmir/CurrencyExchange.git
2. Create a virtual environment (optional but recommended):
bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:

bash
pip install -r requirements.txt

4. create super user
bash
python manage.py createsuperuser

5. Run the development server:
bash
python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000/ to view the application.

# Usage
Navigate to the home page to view all currencies.
Use the provided forms to create, update, or delete currencies.
Access the API endpoints for currency rates and conversions via POST requests.
API Endpoints
1. Get Users
Endpoint: /api/users/
Method: POST
Response: List of users with names and emails.
2. Get Currency Rates
Endpoint: /api/currency-rates/
Method: POST
Body:
json
Copy code
{
  "source_currency": "USD",
  "date_from": "2024-01-01",
  "date_to": "2024-01-31"
}
Response: List of currency rates.
3. Convert Amount
Endpoint: /api/convert/
Method: POST
Body:
json
Copy code
{
  "source_currency": "USD",
  "amount": 100,
  "exchanged_currency": "EUR"
}
Response: Converted amount.
Contributing
We welcome contributions to this project! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch: git checkout -b feature/YourFeature.
Make your changes and commit them: git commit -m 'Add some feature'.
Push to the branch: git push origin feature/YourFeature.
Create a pull request.

# NOTE

1. please use admin panel to change the default provider. 

2. admin creds  (admin,onicra@12345)

