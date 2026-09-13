# Stock Portfolio Tracker

# Manually defined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

total_investment = 0
investments=[]

print(" STOCK PORTFOLIO TRACKER ")

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please choose from:")
        print(", ".join(stock_prices.keys()))
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment
    investments.append(f"{stock}:{quantity} shares * ${price}=${investments}")

    print(f"{stock}: {quantity} shares *${price} = ${investment}")
    print()

print(f"Total Investment: ${total_investment}")

# Save result to a text file
with open("portfolio_result.txt", "w") as file:
    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("------------------\n")
    for item in investments:
        file.write(item+"\n")
    file.write("-------------\n")    
    file.write(f"Total Investment: ${total_investment}\n")

print("Result saved to portfolio_result.txt")