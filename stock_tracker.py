# Stock prices dictionary
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_value = 0

print("Stock Portfolio Tracker")
print("Type 'done' to finish\n")

while True:
    stock = input("Enter stock name: ").upper()

    if stock == "DONE":
        break

    if stock not in stocks:
        print("Stock not available")
        continue

    quantity = int(input("Enter quantity: "))

    value = stocks[stock] * quantity
    total_value += value

    print(f"{stock} investment value = ${value}")

print("\nTotal Portfolio Value =", total_value)

# Save result to file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Portfolio Value: ${total_value}")

print("Portfolio saved to portfolio.txt")
