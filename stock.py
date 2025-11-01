import requests

API_KEY = "YOUR_TWELVE_DATA_KEY"
symbol = "RELIANCE.NS"

url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey={API_KEY}"
resp = requests.get(url).json()
price = float(resp["price"])
print("Current price:", price, "INR")
