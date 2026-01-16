

import logging
from binance import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException

# ---------------- LOGGING CONFIG ----------------
logging.basicConfig(
    filename="trading_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- BASIC BOT ----------------
class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)

        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logging.info("Trading bot initialized (Testnet=%s)", testnet)

    # ----------- SET LEVERAGE -----------
    def set_leverage(self, symbol, leverage):
        try:
            self.client.futures_change_leverage(
                symbol=symbol,
                leverage=leverage
            )
            logging.info("Leverage set to %sx for %s", leverage, symbol)
        except Exception as e:
            logging.error("Failed to set leverage: %s", e)

    # ----------- BALANCE CHECK -----------
    def get_usdt_balance(self):
        try:
            balances = self.client.futures_account_balance()
            for b in balances:
                if b["asset"] == "USDT":
                    return float(b["balance"])
        except Exception as e:
            logging.error("Failed to fetch balance: %s", e)
        return 0.0

    # ----------- MARKET ORDER -----------
    def place_market_order(self, symbol, side, quantity):
        try:
            logging.info("Placing MARKET order: %s %s %s", side, quantity, symbol)
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logging.info("Order response: %s", order)
            return order
        except (BinanceAPIException, BinanceOrderException) as e:
            logging.error("Market order failed: %s", e)
            print("ERROR:", e)
            return None

    # ----------- LIMIT ORDER -----------
    def place_limit_order(self, symbol, side, quantity, price):
        try:
            logging.info("Placing LIMIT order: %s %s %s @ %s", side, quantity, symbol, price)
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
            logging.info("Order response: %s", order)
            return order
        except (BinanceAPIException, BinanceOrderException) as e:
            logging.error("Limit order failed: %s", e)
            print("ERROR:", e)
            return None

    # ----------- STOP-LIMIT ORDER (BONUS) -----------
    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            logging.info(
                "Placing STOP-LIMIT order: %s %s %s stop=%s limit=%s",
                side, quantity, symbol, stop_price, limit_price
            )
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=limit_price,
                stopPrice=stop_price,
                timeInForce="GTC"
            )
            logging.info("Order response: %s", order)
            return order
        except (BinanceAPIException, BinanceOrderException) as e:
            logging.error("Stop-Limit order failed: %s", e)
            print("ERROR:", e)
            return None


# ---------------- CLI INTERFACE ----------------
def main():
    print("\n=== Binance Futures Testnet Trading Bot ===")

    api_key = input("Enter API Key: ").strip()
    api_secret = input("Enter API Secret: ").strip()

    bot = BasicBot(api_key, api_secret, testnet=True)

    symbol = input("Enter trading symbol (e.g. BTCUSDT): ").upper().strip()
    side = input("Order side (BUY / SELL): ").upper().strip()

    if side not in ["BUY", "SELL"]:
        print("Invalid order side")
        return

    # Set leverage (safe default)
    bot.set_leverage(symbol, 10)

    # Balance check
    balance = bot.get_usdt_balance()
    print(f"Available USDT Balance: {balance}")

    if balance <= 0:
        print("Insufficient balance. Cannot place order.")
        return

    print("\nOrder Types:")
    print("1. Market Order")
    print("2. Limit Order")
    print("3. Stop-Limit Order (Bonus)")

    order_type = input("Choose order type (1/2/3): ").strip()

    while True:
        quantity_input = input("Enter quantity: ").strip()
        if quantity_input == "":
            print("Quantity cannot be empty. Please enter a number.")
            continue
        try:
            quantity = float(quantity_input)
            break
        except ValueError:
            print("Invalid number. Try again.")

        
        return

    if order_type == "1":
        order = bot.place_market_order(symbol, side, quantity)

    elif order_type == "2":
        try:
            price = float(input("Enter limit price: "))
        except ValueError:
            print("Price must be a number")
            return
        order = bot.place_limit_order(symbol, side, quantity, price)

    elif order_type == "3":
        try:
            stop_price = float(input("Enter stop price: "))
            limit_price = float(input("Enter limit price: "))
        except ValueError:
            print("Prices must be numbers")
            return
        order = bot.place_stop_limit_order(
            symbol, side, quantity, stop_price, limit_price
        )
    else:
        print("Invalid order type")
        return

    if order:
        print("\nOrder placed successfully!")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Symbol:", order.get("symbol"))
        print("Type:", order.get("type"))
        print("Side:", order.get("side"))
    else:
        print("\nOrder placement failed. Check logs.")


if __name__ == "__main__":
    main()

