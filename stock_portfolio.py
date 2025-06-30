# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300,
    "MSFT": 290
}

# Dictionary to store user input
portfolio = {}

# Take user input
print("Enter your stock holdings (type 'done' to finish):")
while True:
    stock_name = input("Stock Symbol (e.g., AAPL): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("Stock not in our price list. Try again.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock_name}: "))
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_value = 0
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Optional: Save to a text file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    filename = "portfolio_summary.txt"
    with open(filename, "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}")
    print(f"Saved to {filename}")
