# Perfect Money® e-Voucher Activator

# Description:
 This Python script allows you to validate a Perfect Money® e-Voucher using their API. It sends a request
 with your account details and the e-Voucher information to the Perfect Money server. The server responds
 with the validation result, indicating whether the e-Voucher is valid or not.
 
# Requirements:
 - Python 3.x
 - The `requests` library (Install using: pip install requests)

# Instructions:
 1. Make sure you have Python and the `requests` library installed.
 2. Replace the placeholder values in the 'account_id', 'passphrase', 'ev_number', 'ev_code', and 'Payee_Account'
    variables with your actual Perfect Money® account details and e-Voucher information.
 3. Run the script. It will send a POST request to the Perfect Money API and print the validation result.

# Note:
- Perfect Money will send you an HTML containing result. there could be some errors you should consider (invalid ev_number, too many tries, wrong payee account or currency)
 - This script is for educational purposes and to showcase how to interact with the Perfect Money® API.
 - Make sure to keep your account details and e-Voucher information secure and do not share them publicly.
