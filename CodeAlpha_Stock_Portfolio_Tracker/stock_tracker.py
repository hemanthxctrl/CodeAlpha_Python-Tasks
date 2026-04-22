import csv

# Hardcoded stock prices
STOCK_PRICES = {
    "APPLE": 180,
    "TESLA": 250,
    "GOOGLE": 2700,
    "MSFT": 300,
    "AMAZON": 3300
}

portfolio = {}

print("📊 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(STOCK_PRICES.keys()))

# Input loop
while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in STOCK_PRICES:
        print("❌ Stock not available. Try again.")
        continue
    
    try:
        quantity = int(input("Enter quantity: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❌ Invalid quantity. Enter a number.")

# Calculate total investment
total_value = 0
print("\n📈 Portfolio Summary:")
print("-" * 30)

for stock, qty in portfolio.items():
    price = STOCK_PRICES[stock]
    value = price * qty
    total_value += value
    print(f"{stock} -> {qty} shares × ${price} = ${value}")

print("-" * 30)
print(f"💰 Total Investment Value: ${total_value}")

# Save option
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    file_type = input("Save as 'txt' or 'csv'?: ").lower()

    if file_type == "txt":
        with open("portfolio.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("-" * 30 + "\n")
            for stock, qty in portfolio.items():
                price = STOCK_PRICES[stock]
                value = price * qty
                f.write(f"{stock} -> {qty} × ${price} = ${value}\n")
            f.write("-" * 30 + "\n")
            f.write(f"Total Value: ${total_value}\n")
        print("✅ Saved as portfolio.txt")

    elif file_type == "csv":
        with open("portfolio.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, qty in portfolio.items():
                price = STOCK_PRICES[stock]
                value = price * qty
                writer.writerow([stock, qty, price, value])
            writer.writerow(["", "", "Total", total_value])
        print("✅ Saved as portfolio.csv")

    else:
        print("❌ Invalid file type.")

print("\n🚀 Thank you for using the tracker!")