# Crypto-Trading-Bot
## Overview

This project is a **simplified trading bot** built using Python and the official **Binance Futures API**. The bot interacts with the **Binance Futures Testnet (USDT-M)** and allows users to place market, limit, and stop-limit orders through a **command-line interface (CLI)**.

The goal of this project is to demonstrate:

* Practical usage of Binance Futures APIs
* Clean and reusable code structure
* Proper input validation
* Logging and error handling

All trades are executed on the **testnet**, so no real funds are used.

---

## Features

* Supports **Binance Futures Testnet (USDT-M)**

* Place **Market Orders**

* Place **Limit Orders**

* Bonus: **Stop-Limit Orders**

* Supports **BUY and SELL** order sides

* **Balance check before placing orders**

* Interactive **CLI-based interface**

* Logs API requests, responses, and errors

* Clean, class-based and reusable design

* Supports **Binance Futures Testnet (USDT-M)**

* Place **Market Orders**

* Place **Limit Orders**

* Bonus: **Stop-Limit Orders**

* Supports **BUY and SELL** order sides

* Interactive **CLI-based interface**

* Logs API requests, responses, and errors

* Clean, class-based and reusable design

---

## Tech Stack

* **Language:** Python 3
* **Library:** python-binance
* **Exchange:** Binance Futures Testnet

---

## Prerequisites

Before running the bot, ensure you have:

1. Python 3.8 or higher installed
2. Binance Futures Testnet account
3. Binance Futures Testnet API Key and Secret

---

## Setup Instructionsd

### 1. Install Dependencies

```bash
pip install python-binance
```

---

### 2. Generate Binance Futures Testnet API Keys

1. Visit: [https://testnet.binancefuture.com](https://testnet.binancefuture.com)
2. Log in
3. Go to **API Management**
4. Create a new API key
5. Enable **Futures Trading** permission

---

## How to Run

1. Save the source code as:

```text
trading_bot.py
```

2. Open a terminal in the same directory
3. Run the bot:

```bash
python trading_bot.py
```

---

## Required Inputs (CLI)

When running the program, you will be prompted for the following inputs:

1. **API Key** – Binance Futures Testnet API key
2. **API Secret** – Binance Futures Testnet API secret
3. **Trading Symbol** – e.g., `BTCUSDT`
4. **Order Side** – `BUY` or `SELL`
5. **Order Type** –

   * `1` → Market Order
   * `2` → Limit Order
   * `3` → Stop-Limit Order
6. **Quantity** – Futures contract quantity
7. **Price Inputs** – Required for limit and stop-limit orders

---

## Sample Run Output

```text
Enter trading symbol (e.g. BTCUSDT): BTCUSDT
Order side (BUY / SELL): BUY
Choose order type (1/2/3): 1
Enter quantity: 0.01

Order placed successfully!
Order ID: 11729450007
Status: NEW
Symbol: BTCUSDT
Type: MARKET
Side: BUY
```

---

## Logging

All API interactions and errors are logged to:

```text
trading_bot.log
```

This includes:

* Order requests
* API responses
* Error messages

---

## Error Handling

The bot gracefully handles:

* Invalid API credentials
* Insufficient margin
* Invalid symbols
* Quantity and precision errors

Errors are logged and do not crash the application.

---

## Notes on Order Status

* Market orders may initially return status `NEW`
* Binance processes orders asynchronously
* Final order status can be queried via the Futures API

---

## Future Improvements

Possible enhancements include:

* Order status polling to track final execution state
* Strategy-based execution (Grid / TWAP)
* Web-based UI (Flask / React)
* WebSocket-based live updates

Possible enhancements include:

* Balance checks before placing orders
* Order status polling
* Strategy-based execution (Grid / TWAP)
* Web-based UI (Flask / React)
* WebSocket-based live updates

---

## Disclaimer

This project is for **educational and evaluation purposes only** and uses the **Binance Testnet**. No real funds are involved.

---

## Author

Nikita Chavan

Nikita Chavan
