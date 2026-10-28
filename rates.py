import argparse
import sys
import requests

API_URL = "https://www.cbr-xml-daily.ru/daily_json.js"


def get_rates() -> dict:
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"Ошибка при подключении к сервису ЦБ РФ: {err}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Курсы валют ЦБ РФ")
    parser.add_argument("codes", nargs="*", default=["USD", "EUR", "CNY"],
                        help="Коды валют, например: USD EUR")
    args = parser.parse_args()

    data = get_rates()
    print(f"Курсы на {data['Date'][:10]}:")
    print(f"Предыдущий курс: {data['PreviousDate'][:10]}")
    for code in args.codes:
        item = data["Valute"].get(code.upper())
        if item is None:
            print(f"  {code}: не найдено")
            continue
        rate = item["Value"] / item["Nominal"]
        print(f"  {code.upper()}: {rate:.2f} ₽")


if __name__ == "__main__":
    main()
