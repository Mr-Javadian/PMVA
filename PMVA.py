import requests


def validate_perfect_money_voucher(account_id, passphrase, ev_number, ev_code, Payee_Account):
    url = "https://perfectmoney.com/acct/ev_activate.asp"
    data = {
        "AccountID": account_id,
        "PassPhrase": passphrase,
        "ev_number": ev_number,
        "ev_code": ev_code,
        "Payee_Account": Payee_Account
    }

    response = requests.post(url, data=data)
    result = response.text  # The API response will contain the validation result

    print(result)


# Replace these with your actual Perfect Money® account details and e-Voucher number
account_id = "xxxxxxxxxxxx"
passphrase = "xxxxxxxxxxxx"
ev_number = "xxxxxxxxxxxx"
ev_code = "xxxxxxxxxxxx"
Payee_Account = "xxxxxxxxxxxx"

validate_perfect_money_voucher(
    account_id, passphrase, ev_number, ev_code, Payee_Account)
