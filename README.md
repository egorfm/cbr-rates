<h1 align="center">💱 cbr-rates</h1>

<p align="center">
  Быстрый консольный скрипт для получения <b>официальных курсов валют ЦБ РФ</b> 🇷🇺
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/API-ЦБ%20РФ-2ea44f" alt="CBR API">
  <img src="https://img.shields.io/badge/CLI-argparse-orange" alt="CLI">
  <img src="https://img.shields.io/badge/status-working-brightgreen" alt="Status">
</p>

---

✨ Возможности

- 💵 Показывает курсы USD, EUR, CNY по умолчанию
- 🔎 Можно выбрать любые другие валюты прямо в команде
- 📅 Выводит дату курса и дату предыдущего курса
- ⚡ Лёгкий скрипт: всего одна зависимость (`requests`)

🚀 Установка

```bash
1. Клонируем репозиторий
git clone https://github.com/egorfm/cbr-rates.git
cd cbr-rates

2. Создаём и включаем виртуальное окружение
python3 -m venv .venv
source .venv/bin/activate

3. Ставим зависимости
pip install -r requirements.txt
```

🛠 Использование

```bash
python rates.py            # курсы по умолчанию: USD, EUR, CNY
python rates.py USD GBP    # только выбранные валюты
python rates.py --list     # список всех доступных валют
```

📸 Пример вывода

```
Курсы на 2026-10-17:
Предыдущий курс: 2026-10-16
  USD: 83.62 ₽
  EUR: 93.72 ₽
  CNY: 12.49 ₽
```

🧰 Технологии

|-----|-------|
| 🐍 Python | основной язык |
| 🌐 requests | запросы к API |
| 🧾 argparse | аргументы командной строки |
| 🏦 cbr-xml-daily.ru | источник данных |

> 🕒 Курсы ЦБ обновляются в **рабочие дни**. В выходные скрипт показывает последний опубликованный курс.

