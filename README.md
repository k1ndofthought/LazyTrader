# LazyTrader - NASDAQ Checklist + Risk Calculator

LazyTrader is a simple Python app that helps traders manage a **checklist**, calculate **risk based on account balance**, and **open trading websites** automatically (TradingView & ForexFactory).

---

## Features

* Checklist for your trading setup
* Background turns **green** when all items are checked
* Risk calculator that automatically calculates **your risk amount** based on your balance (default 1.2%)
* Automatically opens **TradingView** and **ForexFactory Calendar** in Firefox
* Fully **configurable via `config.json`**

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/YourUsername/LazyTrader.git
cd LazyTrader
```

2. **Install Python dependencies**

```bash
pip install -r requirements.txt
```

*(Currently uses only `tkinter`, which is included in standard Python.)*

3. **Edit `config.json` (optional)**

* `risk_percent` → set your preferred risk percentage
* `checklist_items` → add/remove checklist items
* `urls` → add/remove websites to open

---

## Usage

**Run the app:**

```bash
python LazyTrader.py
```

* The app will open your browser to TradingView and ForexFactory
* The checklist window will appear on top
* Enter your account balance → risk amount is calculated automatically

**Build an EXE (optional):**

```bash
pyinstaller --onefile --noconsole LazyTrader.py
```

* EXE will be in `dist\LazyTrader.exe`
* Place `config.json` in the same folder as the EXE

---

## Config Example (`config.json`)

```json
{
  "risk_percent": 1.2,
  "checklist_items": [
    "HTF Bias",
    "Liquidity Sweep",
    "NY Session",
    "Risk <1%",
    "News Checked"
  ],
  "urls": [
    "https://www.tradingview.com",
    "https://www.forexfactory.com/calendar"
  ]
}
```

---

## Notes

* Make sure **Firefox** is installed at the path in the script:

```python
firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
```

* You can update the checklist and websites without rebuilding the EXE

---

## License

MIT License (free to use and modify)
