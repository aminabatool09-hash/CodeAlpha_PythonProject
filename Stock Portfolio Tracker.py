stock_prices = {
    "PTCL": 15,
    "UBL": 120,
    "HBL": 100
}

total = 0

print("Stock Portfolio")

while True:
    stock = input("Enter stock name (or done): ")

    if stock == "done":
        break

    if stock in stock_prices:
        qty = int(input("Enter quantity: "))
        total = total + (stock_prices[stock] * qty)
    else:
        print("Stock not found")

print("Total Investment =", total)