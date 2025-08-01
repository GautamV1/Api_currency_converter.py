import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    response = requests.get(url , verify= True)

    if response.status_code == 200:
        data = response.json()
        print("DEBUG API RESPONSE:", data)
        result = data["rates"].get(to_currency.upper())

        if result is not None:
            print(f"\n {amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
            return result
        else:
            print("Invalid currency code or conversion failed")
            return None
    else:
        print("Failed to fetch exchange rate.try again.")
        return None

def main():
    print("Live currency converter(via exchangerate.host)")
    try:
        amount = float(input("Enter amount:"))
        from_currency = input("From Currency (e.g. USD): ").strip().upper()
        to_currency = input("To Currency(e.g. INR): ").strip().upper()
        convert_currency(amount , from_currency, to_currency)
    except ValueError:
        print("Invalid Input. please enter valid number.")

if __name__ == "__main__":
    main()