

class MpesaPayment:
    """
    Handles M-Pesa payment integration.
    """
    
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
    
    def make_payment(self, amount, phone_number):
        """
        Initiates an M-Pesa payment.
        """
        # Your code for making M-Pesa payments goes here.

class MpesaPaymentResponse:
    """
    Represents the response from an M-Pesa payment.
    """
    
    def __init__(self, success, message):
        self.success = success
        self.message = message

 # mpesa.py

import requests

class MpesaPayment:
    """
    Handles M-Pesa payment integration.
    """

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = 'https://api.mpesa.com'

    def make_payment(self, amount, phone_number):
        """
        Initiates an M-Pesa payment.

        Args:
            amount (float): The payment amount.
            phone_number (str): The customer's phone number.

        Returns:
            MpesaPaymentResponse: Response object with success and message.
        """
        url = f'{self.base_url}/v1/payments'
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }
        payload = {
            'amount': amount,
            'phone_number': phone_number,
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                return MpesaPaymentResponse(True, 'Payment successful.')
            else:
                return MpesaPaymentResponse(False, 'Payment failed.')
        except Exception as e:
            return MpesaPaymentResponse(False, str(e))

class MpesaPaymentResponse:
    """
    Represents the response from an M-Pesa payment.
    """

    def __init__(self, success, message):
        self.success = success
        self.message = message
       
