import requests

NBU_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CURRENCIES = ["EUR", "USD", "PLN"]

def get_rate(code):
    response = requests.get(NBU_URL, params={"valcode": code, "json": ""}, timeout=10)
    response.raise_for_status()
    data = response.json()
    if not data:
        raise ValueError(f"НБУ не повернув дані для {code}")
    return data[0]["rate"]

def main():
    while True:
        code = input(f"Тип валюти {'/'.join(CURRENCIES)}: ").strip().upper()
        if code in CURRENCIES:
            break
        print("Непідтримувана валюта.")
    while True:
        try:
            amount = float(input("Кількість: ").replace(",", "."))
            if amount < 0:
                raise ValueError
            break
        except ValueError:
            print("Введіть невід'ємне число.")
    try:
        rate = get_rate(code)
    except (requests.RequestException, ValueError) as e:
        print(f"Не вдалося отримати курс: {e}")
        return
    print(f"Курс НБУ: 1 {code} = {rate} UAH")
    print(f"{amount} {code} = {amount * rate:.2f} UAH")

if __name__ == "__main__":
    main()
